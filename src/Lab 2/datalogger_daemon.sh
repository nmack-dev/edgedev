#!/bin/bash

# Set the name of the python program
PYSCRIPT=sensor_datalogger.py

# Generate pid and log filenames
RUNDIR=~/.run
PIDFILE="$RUNDIR/${PYSCRIPT%.*}.pid"
LOGFILE="$RUNDIR/${PYSCRIPT%.*}.log"

start() {
	# Check that the run directory exists and create it if not
	if [ ! -d "$RUNDIR" ] && ! mkdir "$RUNDIR"; then
		echo "Unable to create directory $RUNDIR"
		return 1
	fi

	# Check if the program is already running
	if [ -f "$PIDFILE" ] && kill -0 $(cat "$PIDFILE"); then
		echo "Daemon already running" >&2
		return 1
	fi

	echo "Starting daemon..." >&2
	nohup python3 "$PYSCRIPT" > /dev/null 2>> "$LOGFILE"  & echo $! > "$PIDFILE"
	echo "Daemon started [`cat $PIDFILE`]" >&2
}

stop() {
	# Check if the program is running
	if [ ! -f "$PIDFILE" ] || ! kill -0 $(cat "$PIDFILE"); then
		echo "Daemon not running" >&2
		return 1
	fi

	echo 'Stopping daemon...' >&2
	kill $(cat "$PIDFILE") && rm -f "$PIDFILE"
	echo "Daemon stopped" >&2	
}

status() {
	if [ -f "$PIDFILE" ] && kill -0 $(cat "$PIDFILE"); then
		echo "Daemon is running" >&2
	else
		echo "Daemon is not running" >&2
	fi
}

case "$1" in
	start)
		start
		;;
	stop)
		stop
		;;
	status)
		status
		;;
	restart)
		stop
		start
		;;
	*)
		echo "Usage: $0 {start|stop|status|restart}"
esac
