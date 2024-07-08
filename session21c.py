from session21B import mongodbhelper
from session21A import User

def main():
    print("welcome to mongodb test app")
    dbhelper=mongodbhelper()
    """
    user=User()
    user.add_user()
    document=vars(user)
    dbhelper.insert(document)
    """

    users=dbhelper.fetch()
    for user in users:
        print(user)

if __name__=="__main__":
    main()