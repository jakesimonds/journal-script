BASE_DIR="$(dirname "$0")"

ENTRY_DIR="$BASE_DIR/completed-entries/2023"

DEFAULT_TEMPLATE="$BASE_DIR/default-template.txt"
PROMPT_TEMPLATE="$BASE_DIR/prompt-template.txt"

SCRIPT_PATH="$BASE_DIR/scripts/new-entry.py"

CURRENT_DATE=$(date +"%Y-%m-%d_%H-%M-%S")


if [[ "$1" == "-p" ]]; then
    TEMPLATE=$PROMPT_TEMPLATE
    NEW_ENTRY_PATH="$ENTRY_DIR/$CURRENT_DATE.txt"
    cp $TEMPLATE $NEW_ENTRY_PATH
    python3 $SCRIPT_PATH $NEW_ENTRY_PATH
else
    TEMPLATE=$DEFAULT_TEMPLATE
    NEW_ENTRY_PATH="$ENTRY_DIR/$CURRENT_DATE.txt"
    cp $TEMPLATE $NEW_ENTRY_PATH
    python3 $SCRIPT_PATH $NEW_ENTRY_PATH
fi


if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open file.txt
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open -a TextEdit file.txt
fi

