def pre_process(content=""):
    text = content.splitlines()
    final_text = ""
    for i in text:
        if len(i) > 1:
            final_text += " "+i

    return final_text
