#!/usr/bin/env bash
{ set +x; } 2>/dev/null

path=~/.Tests
[[ -z "$TESTS_URL" ]] && {
	echo "DEBUG: \$TESTS_URL NOT DEFINED"
	txt="${BASH_SOURCE[0]%/*}/url.txt"
	TESTS_URL="$(set -x; cat "$txt")" || exit
}

# known-issues: ssh permissions with urls like 'git@github.com:owner/repo.git'
# fix: https url - 'https://github.com/owner/repo.git' 
( set -x; git clone --depth 1 "$TESTS_URL" "$path" ) || exit
