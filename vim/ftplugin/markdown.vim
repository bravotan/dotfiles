call SetupWrapping()

au BufWritePre <buffer> :call CleanTrailingSpace()

map <buffer> <Leader>m :Mm <CR>
