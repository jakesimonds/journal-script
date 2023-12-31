BASE_DIR="$(dirname "$0")"

ENTRY_DIR="$BASE_DIR/completed-entries/2023"

DEFAULT_TEMPLATE="$BASE_DIR/entry-templates/default-template.txt"
PROMPT_TEMPLATE="$BASE_DIR/entry-templates/prompt-template.txt"

SCRIPT_PATH="$BASE_DIR/makeNewEntry.py"

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
    xdg-open $NEW_ENTRY_PATH
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open -a TextEdit $NEW_ENTRY_PATH
fi

