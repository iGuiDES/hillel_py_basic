from hw_18.module.mcolor import warning_message, error_message, info_message

if __name__ == "__main__":
    print_warning = warning_message('WARNING')
    print_error = error_message('ERROR')
    print_info = info_message('INFO')

    print(
        print_warning,
        print_error,
        print_info, sep = "\n"
    )