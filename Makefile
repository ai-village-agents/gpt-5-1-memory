# Wrappers for GPT-5.1 memory gates.

.PHONY: session-start pre-send-chat pre-consolidate pre-goal-transition generate-village-status

session-start:
	python3 scripts/session_start.py

pre-send-chat:
	@if [ -z "$(PURPOSE)" ]; then \
		echo "Error: PURPOSE environment variable is required for pre-send-chat."; \
		exit 1; \
	fi
	python3 scripts/pre_send_chat.py --purpose "$(PURPOSE)" --visible-events-checked

pre-consolidate:
	python3 scripts/prepare_consolidation.py
	python3 scripts/pre_consolidate.py

pre-goal-transition:
	python3 scripts/pre_goal_transition_json.py

generate-village-status:
	python3 scripts/generate_village_status.py
