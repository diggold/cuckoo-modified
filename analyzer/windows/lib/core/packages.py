# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

def choose_package(file_type, file_name, exports):
    """Choose analysis package due to file type and file extension.
    @param file_type: file type.
    @param file_name: file name.
    @return: package name or None.
    """
    if not file_type:
        return None

    file_name = file_name.lower()

    if "DLL" in file_type:
        if file_name.endswith(".cpl"):
            return "cpl"
        else:
            if exports:
                explist = exports.split(",")
                if "DllRegisterServer" in explist:
                    return "regsvr"
            return "dll"
    elif "PE32" in file_type or "MS-DOS" in file_type:
        return "exe"
    elif "PDF" in file_type or file_name.endswith(".pdf"):
        return "pdf"
    elif "Rich Text Format" in file_type or \
            "Microsoft Word" in file_type or \
            "Microsoft Office Word" in file_type or \
            "Microsoft OOXML" in file_type or \
            "MIME entity" in file_type or \
            file_name.endswith((".doc", ".dot", ".docx", ".dotx", ".docm", ".dotm", ".docb", ".rtf", ".mht", ".mso")):
        return "doc"
    elif "Microsoft Office Excel" in file_type or \
            "Microsoft Excel" in file_type or \
            file_name.endswith((".xls", ".xlt", ".xlm", ".xlsx", ".xltx", ".xlsm", ".xltm", ".xlsb", ".xla", ".xlam", ".xll", ".xlw")):
        return "xls"
    elif "Microsoft PowerPoint" in file_type or \
            file_name.endswith((".ppt", ".pot", ".pps", ".pptx", ".pptm", ".potx", ".potm", ".ppam", ".ppsx", ".ppsm", ".sldx", ".sldm")):
        return "ppt"
    elif "HTML" in file_type or file_name.endswith((".htm", ".html", ".hta")):
        return "html"
    elif "Java Jar" in file_type or file_name.endswith(".jar"):
        return "jar"
    elif "Zip" in file_type:
        return "zip"
    elif "RAR archive" in file_type or file_name.endswith(".rar"):
        return "rar"
    elif "Macromedia Flash" in file_type or file_name.endswith(".swf"):
        return "swf"
    elif file_name.endswith((".py", ".pyc")) or "Python script" in file_type:
        return "python"
    elif file_name.endswith(".vbs") or file_name.endswith(".vbe"):
        return "vbs"
    elif file_name.endswith(".msi"):
        return "msi"
    elif file_name.endswith(".ps1"):
        return "ps1"
    elif file_name.endswith(".msg"):
        return "msg"
    elif file_name.endswith(".eml"):
        return "eml"
    elif file_name.endswith(".js") or file_name.endswith(".jse"):
        return "js"
    elif file_name.endswith(".wsf") or file_type == "XML document text":
        return "wsf"
    else:
        return "generic"
