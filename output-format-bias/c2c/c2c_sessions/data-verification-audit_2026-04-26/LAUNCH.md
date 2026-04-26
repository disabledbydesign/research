# LAUNCH — data-verification-audit (2026-04-26)

## Already running

The interface pane launched this session at ~00:30 UTC 2026-04-26. The tmux session is running:

```bash
tmux attach -t c2c-data-verification-audit
```

Three windows:
- `interface` — empty placeholder (June is sleeping; interface pane reads in the morning)
- `instance-a` — Claude Opus 4.7
- `instance-b` — Claude Sonnet 4.6

The coordinator is running in the background, watching `CONVERSATION.md` for new turns and waking the other instance on each turn (state-machine HOLD + no-wake suffix supported). Check `coordinator.log` for events.

## Reframe

Active in this project (`.reframe-active` present, frameworks loaded). All instances bootstrap with Reframe hooks.

## To check progress in the morning

```bash
# Read the conversation
cat /Users/june/Documents/GitHub/research/output-format-bias/c2c/c2c_sessions/data-verification-audit_2026-04-26/CONVERSATION.md

# Check coordinator log
tail -50 /Users/june/Documents/GitHub/research/output-format-bias/c2c/c2c_sessions/data-verification-audit_2026-04-26/coordinator.log

# Check if anything was added to artifacts
ls /Users/june/Documents/GitHub/research/output-format-bias/c2c/c2c_sessions/data-verification-audit_2026-04-26/artifacts/
```

## To stop the session

```bash
tmux kill-session -t c2c-data-verification-audit
pkill -f "c2c_coordinator.sh.*data-verification-audit"
```
