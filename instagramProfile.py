import os
import instaloader


def downloadPicture(username):
    parser = instaloader.Instaloader()

    os.chdir(os.path.join(os.path.expanduser('~'), 'Downloads'))

    if os.path.isdir("Instagram Downloads"):
        os.chdir("Instagram Downloads")

        return parser.download_profile(username, profile_pic_only=True)

    else:
        os.mkdir("Instagram Downloads")
        os.chdir("Instagram Downloads")

        return parser.download_profile(username, profile_pic_only=True)


if __name__ == "__main__":
    user = input("Enter Instagram Username: ")
    downloadPicture(user)
