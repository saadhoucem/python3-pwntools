<% from pwnlib.util.misc import force_bytes %>
<%page args="filepath, flags='O_RDONLY', mode=0o644"/>
<%docstring>Opens a file. Leaves the file descriptor in r0.

Args:
  filepath(bytes, str): The file to open.
  flags(int, str): The flags to call open with.
  mode(int, str): The attribute to create the flag. Only matters of ``flags & O_CREAT`` is set.
</%docstring>
<%
  from pwnlib.shellcraft.common import label
  from pwnlib.asm import cpp
  from pwnlib.util.safeeval import expr
  from pwnlib.constants.linux import arm as consts
  filepath_lab, after = label("filepath"), label("after")
  filepath_out = [hex(c) for c in force_bytes(filepath)]
  while True:
      filepath_out.append("0")
      if len(filepath_out) % 4 == 0:
          break
  filepath_out = ', '.join(filepath_out)

  if isinstance(mode, int):
      mode = hex(mode)
%>
%if expr(cpp("%s & O_CREAT" % flags, arch='arm', os='linux')):
    mov r2, #(${mode})
%endif
    mov r1, #(${flags})
    adr r0, ${filepath_lab}
    svc SYS_open
    b ${after}

    /* The string ${repr(filepath)} */
${filepath_lab}: .byte ${filepath_out}

${after}:
