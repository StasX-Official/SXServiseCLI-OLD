def error(error, dep_code):
    main_error(error, dep_code)

def main_error(error_sxg, code):
    formatted_time = "00.00.00 00:00"
    file = open("logs.txt", "a")
    error_txt = error_sxg

    if code == 0:
        #SXG OTHER ERROR
        code_sys_erro = "OTHER"
        save_error(file, formatted_time, error_txt, code_sys_erro)
    elif code == 1:
        #SXG FUNCTION ERROR
        code_sys_erro = "FUNCTION"
        save_error(file, formatted_time, error_txt, code_sys_erro)
    elif code == 2:
        #SXG SYSTEM ERROR
        code_sys_erro = "SYSTEM"
        save_error(file, formatted_time, error_txt, code_sys_erro)
    else:
        erro_code_auth = "Invalid department code. Error: 7900"
        code_sys_erro = "ERROR_AUTH"
        save_error(file, formatted_time, erro_code_auth, code_sys_erro)


def save_error(file, time, error, code):
    print(time, "SXG - ", error, code)
    text_to_write = f"{time}", error, code, ".\n"
    auth2v = str(text_to_write)
    file.write(auth2v)
    file.close()

testerror = "TEST"
code_test = 3
error(testerror, code_test)