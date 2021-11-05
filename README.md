# runsolver

Runsolver is a tool to set time and memory limits for solvers. This
repository holds a copy of the [runsolver
v3.4.0](http://www.cril.univ-artois.fr/~roussel/runsolver/) source code,
with some minor fixes (see [changelog](src/Changelog)).


## Compile

    cd src
    make -j `nproc`

## Usage

`./runsolver --timestamp -C 1200 -W 180 -R 8192 -V 102400 -w watch.log -v values.log -o tool_output.log ./tool_name tool_args`

1. -C is for CPU time limit in seconds. Sum total of all the threads.
2. -W is the Wall clock time limit in seconds.
3. -R is the maximum resident segment size limit in Mega Bytes.
4. -V is the maximum virtual memory limit in Mega Bytes.
5. -w is the watcher log file. It logs thread specific details.
6. -v is the key value pair log file. Smaller and easier to parse.
7. -o is the log file for stdout and stderr redirect of the tool being run.
