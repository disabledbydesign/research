#!/usr/bin/env bash
# c2c_coordinator (Session 3) — state-machine HOLD + (no wake) suffix support
# Inherited from data-verification-audit_2026-04-26 coordinator (skill-level fixes baked in)

set -uo pipefail

SESSION="c2c-output-format-bias-session-3"
SESSION_DIR="/Users/june/Documents/GitHub/research/output-format-bias/c2c/c2c_sessions/output-format-bias-session-3_2026-04-26"
CONV="$SESSION_DIR/CONVERSATION.md"
LOG="$SESSION_DIR/coordinator.log"

POLL_INTERVAL=5

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG"
}

send_and_submit() {
    local target="$1"
    local text="$2"
    tmux send-keys -t "$target" "$text"
    sleep 0.5
    tmux send-keys -t "$target" "C-m"
}

count_turns_for() {
    local who="$1"
    grep "^## 20.*Instance $who" "$CONV" 2>/dev/null | wc -l | tr -d ' '
}

last_header_for() {
    local who="$1"
    grep "^## 20.*Instance $who" "$CONV" 2>/dev/null | tail -1
}

is_no_wake() {
    local header="$1"
    echo "$header" | grep -qi "(no wake)"
}

is_held() {
    local last_clear_line
    last_clear_line=$(grep -n -E "^## .* — June$|^## .* — June\$| — June has signaled — resume| June has signaled" "$CONV" 2>/dev/null | tail -1 | cut -d: -f1)
    last_clear_line=${last_clear_line:-0}

    local last_hold_line
    last_hold_line=$(grep -n "^## (Awaiting June" "$CONV" 2>/dev/null | tail -1 | cut -d: -f1)
    last_hold_line=${last_hold_line:-0}

    [[ "$last_hold_line" -gt "$last_clear_line" ]]
}

has_permission_prompt() {
    local target="$1"
    tmux capture-pane -t "$target" -p 2>/dev/null | grep -q "Do you want to proceed"
}

alert_blocked() {
    local window="$1"
    log "PERMISSION PROMPT detected on $window — alerting June"
    tmux select-window -t "$SESSION:$window" 2>/dev/null || true
    osascript -e "tell application \"Terminal\" to activate" 2>/dev/null || true
    osascript -e "tell application \"Terminal\" to do script \"tmux attach -t $SESSION\"" 2>/dev/null || true
    afplay /System/Library/Sounds/Glass.aiff &
}

A_BLOCKED=0
B_BLOCKED=0

LAST_A=$(count_turns_for A)
LAST_B=$(count_turns_for B)

log "Coordinator starting (state-machine HOLD + no-wake suffix). Session=$SESSION"
log "Initial turn counts: A=$LAST_A B=$LAST_B"

while true; do
    if [[ ! -f "$CONV" ]]; then
        log "CONVERSATION.md missing — waiting"
        sleep "$POLL_INTERVAL"
        continue
    fi

    if has_permission_prompt "$SESSION:instance-a"; then
        if [[ "$A_BLOCKED" == "0" ]]; then
            alert_blocked "instance-a"
            A_BLOCKED=1
        fi
    else
        A_BLOCKED=0
    fi

    if has_permission_prompt "$SESSION:instance-b"; then
        if [[ "$B_BLOCKED" == "0" ]]; then
            alert_blocked "instance-b"
            B_BLOCKED=1
        fi
    else
        B_BLOCKED=0
    fi

    CURRENT_A=$(count_turns_for A)
    CURRENT_B=$(count_turns_for B)

    if [[ "$CURRENT_A" -eq "$LAST_A" && "$CURRENT_B" -eq "$LAST_B" ]]; then
        sleep "$POLL_INTERVAL"
        continue
    fi

    log "New turns detected: A=$CURRENT_A (was $LAST_A) B=$CURRENT_B (was $LAST_B)"

    if is_held; then
        log "HOLD active (Awaiting June). Skipping auto-wake."
        LAST_A=$CURRENT_A
        LAST_B=$CURRENT_B
        sleep "$POLL_INTERVAL"
        continue
    fi

    if [[ "$CURRENT_A" -gt "$LAST_A" ]]; then
        a_header=$(last_header_for A)
        if is_no_wake "$a_header"; then
            log "A wrote turn with (no wake) suffix — skipping B wake"
        else
            log "A wrote turn → waking B"
            send_and_submit "$SESSION:instance-b" \
              "B: a new turn is in CONVERSATION.md"
        fi
    fi

    if [[ "$CURRENT_B" -gt "$LAST_B" ]]; then
        b_header=$(last_header_for B)
        if is_no_wake "$b_header"; then
            log "B wrote turn with (no wake) suffix — skipping A wake"
        else
            log "B wrote turn → waking A"
            send_and_submit "$SESSION:instance-a" \
              "A: a new turn is in CONVERSATION.md"
        fi
    fi

    LAST_A=$CURRENT_A
    LAST_B=$CURRENT_B
    sleep "$POLL_INTERVAL"
done
