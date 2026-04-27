# Launch — output-format-bias-session-3

## How to attach

```bash
tmux attach -t c2c-output-format-bias-session-3
```

Three windows: `interface`, `instance-a`, `instance-b`.
Switch between windows with `Ctrl+b n` (next) or `Ctrl+b 0/1/2` (by index).
Detach with `Ctrl+b d`.

## What's running

- **A** — Opus 4.7 (`claude-opus-4-7`)
- **B** — Sonnet 4.6 (`claude-sonnet-4-6`)
- Coordinator — `c2c_coordinator.sh` (state-machine HOLD + no-wake suffix support)
- Reframe — active (verified at launch)

## Coordinator log

```bash
tail -f /Users/june/Documents/GitHub/research/output-format-bias/c2c/c2c_sessions/output-format-bias-session-3_2026-04-26/coordinator.log
```

## CONVERSATION.md

```bash
cat /Users/june/Documents/GitHub/research/output-format-bias/c2c/c2c_sessions/output-format-bias-session-3_2026-04-26/CONVERSATION.md
```

## Killing the session at close

```bash
# Stop coordinator
pkill -f "output-format-bias-session-3/c2c_coordinator.sh"

# Kill tmux session
tmux kill-session -t c2c-output-format-bias-session-3
```

## Checkpoint protocol

- The interface pane (this conversation) watches CONVERSATION.md and relays plain-language summaries to June each turn.
- When the session is in `Awaiting June`, the interface pane surfaces specific decisions June needs to make.
- June can write directly to CONVERSATION.md as `## YYYY-MM-DD HH:MM UTC — June` at any time.
- The interface pane sends wake commands on June's behalf; the coordinator does not auto-wake during HOLD.
