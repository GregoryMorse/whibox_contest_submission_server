flash_categories = {'success': 'success',
                    'info': 'info',
                    'warning': 'warning',
                    'danger': 'danger'}

flash_texts_and_categories = {
    'ACCOUNT_UPDATE_FAILED': ('Failed to update your display name.', flash_categories['danger']),
    'ACCOUNT_UPDATED': ('Display name updated.', flash_categories['success']),
    'BAD_USERNAME_OR_PWD': ('Bad username or password', flash_categories['danger']),
    'WELCOME_BACK': ('Welcome back %s', flash_categories['success']),
    'LOGOUT': ('You have logged out', flash_categories['info']),
    'ACCOUNT_CREATED': ('A new account was created for the user %s!', flash_categories['info']),
    'ONLY_EXT_IS_C': ('The only allowed file extension is ".c"', flash_categories['warning']),
    'CHALLENGE_SUBMITTED': ('Your challenge has been submitted!', flash_categories['info']),
    'INVALID_KEY': ('The key must be a 32-character string of hexadecimal digits.', flash_categories['warning']),
    'EMAIL_MUST_MATCH': ('Emails must match', flash_categories['warning']),
    'PWD_MUST_MATCH': ('Passwords must match', flash_categories['warning']),
    'CANNOT_BREAK_OWN': ('You cannot break your own candidates.', flash_categories['warning']),
    'CANNOT_BREAK_TWICE': ('You cannot break the same candidate twice.', flash_categories['warning']),
    'CANNOT_INVERT_OWN': ('You cannot invert your own candidates.', flash_categories['warning']),
    'CANNOT_INVERT_TWICE': ('You cannot invert the same candidate twice.', flash_categories['warning']),
    'CORRECT_KEY': ('Your key is correct !', flash_categories['success']),
    'PLEASE_SIGN_IN': ('Please sign in to access this page', flash_categories['warning']),
    'ERROR_USER_EXISTS': ('An error occurred. The username/nickname/email might be already taken.', flash_categories['danger']),
    'ERROR_UNKNOWN': ('An error occurred. Please consider notify the orgnizing committee.', flash_categories['danger']),
}
