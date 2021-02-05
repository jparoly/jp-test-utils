Usage:

    ./mini-df [-h] [PATH...]

`mini-df` outputs the file system disk space usage of each entry in
PATH. The information required is: Total Space, Free Space, Used
Space. The result should be in Bytes.

- PATH can be zero or more arguments. IF zero args are given,
  `mini-df` will list the disk space usage of the current directory.
- If given `-h` will output the result in human-readable format.

