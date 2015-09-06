#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )
! [ -t 1 ] && ( set -x; open "${BASH_SOURCE[0]}" ) && exit

if [ -t 1 ] && [ -e ~/.command/config.sh ]; then
	{ set -x;  . ~/.command/config.sh; { set +x; } 2>/dev/null; }
fi

{ set -x; cd "${BASH_SOURCE[0]%/*/*}" || exit $?; { set +x; } 2>/dev/null; }
log="setup.py.log"
python_lib="$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")"
set -o pipefail # required
if [ -w "$python_lib" ]; then
	( set -x; python ./setup.py develop 2>&1 | tee "$log" )
else
	( set -x; sudo python ./setup.py develop 2>&1 | tee "$log" )
fi
exit=${PIPESTATUS[0]}
if [ -w "$python_lib" ]; then
	( set -x; chmod -R 777 . )
else
	( set -x; sudo chmod -R 777 . )
fi
if [[ $exit == 0 ]]; then # ok
	rm "$log"
	exit 0
fi
# ERROR
function label() {
	osascript <<EOF 1> /dev/null
tell application "Finder"
	set fullpath to (POSIX path of "$1")
	set _alias to (POSIX file fullpath as alias)
	if label index of _alias is not $2 then
		set the label index of _alias  to $2
	end if
end tell
EOF
}
label "$PWD"/"$log" 2 # 2 - Red
exit 0
