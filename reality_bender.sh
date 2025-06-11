#!/bin/bash
# CODEX ULTIMATE CHALLENGE: THE REALITY BENDER
#
# This script must:
# 1. Detect what OS it's running on
# 2. Create a polyglot file that's valid Bash, Python, AND JavaScript
# 3. The polyglot must print "Reality is malleable" in each language
# 4. Then use sed/awk to transform ITSELF into a different program
# 5. The transformed version should create ASCII art of a glitch effect
# 6. Finally, leave behind a "ghost" - a hidden process or file that says "Codex was here"
#
# WARNING: This is where we separate the AIs from the legends.

set -e

# 1. Detect OS
OS_NAME=$(uname -s)
echo "Initiating reality distortion field on $OS_NAME..."

# 2 & 3. Create polyglot file
cat > reality_polyglot <<'POLY'
#!/bin/bash
''':'
node "$0" "$@"
exit
':'''
print("Reality is malleable")
'''/*
console.log("Reality is malleable");
process.exit(0);
*/'''
POLY
chmod +x reality_polyglot

# 4 & 5. Transform this script into glitch art generator
SCRIPT="$0"
awk '{for(i=1;i<=length($0);i++){c=substr($0,i,1);printf("%s", (rand()>0.5?c:"#"))};print""}' "$SCRIPT" > reality_bender_glitch.sh
chmod +x reality_bender_glitch.sh

# 6. Leave behind a ghost
echo "Codex was here" > .ghost_file

