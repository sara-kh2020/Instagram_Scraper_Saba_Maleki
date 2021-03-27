

from instapy import InstaPy
from instapy.util import smart_run
from instapy.util import get_relationship_counts

def getPercentageCount(followers, percent):
	return int((followers*percent)/100)


# login credentials
# insta_username = 'saba_insta1' #ban shode
# insta_password = '123456saba'
insta_username = 'saba_insta2' #ban nashode
insta_password = '123456saba'
# insta_username = 'saba_insta3'
# insta_password = '123456saabaa'

targetAccount = "idealofficial"
percentage=100

print ('[INFO] Extracting '  + ' the followers from ' + targetAccount)
flag=True

    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)
while(flag):
    session.set_quota_supervisor(enabled=True, sleep_after=['server_calls'], sleepyhead=True, stochastic_flow=True, notify_me=True,
                          peak_server_calls_hourly=150, peak_server_calls_daily=3000 )
    # session.set_quota_supervisor(enabled=True, sleep_after=['server_calls'], sleepyhead=True, stochastic_flow=True, notify_me=True,
    #                       peak_server_calls_daily=152 )
    
    print ('[INFO]: Logging in..')
    try:
        with smart_run(session):
        	#get follower, following count
        
            followers_count, following_count = get_relationship_counts(session.browser, targetAccount, session.logger)
        
        
            amount = getPercentageCount(int(followers_count),percentage)
            print ('[INFO] Going to extract ' + str(amount) + ' followers out of ' + str(followers_count))
            followers_list = session.grab_followers(username=targetAccount, amount=amount, live_match=False, store_locally=True)
            print ('[INFO]: Followers grabbed successfully. Saving to file..')
            result = ''
            for el in followers_list:
                result = result + el + '\n'
            with open("./" + str(targetAccount) + "_followers_new2.txt", "w") as text_file:
                text_file.write(result)
            
            print ('[INFO]: Followers list successfully saved to ' + targetAccount + '_followers.txt')
            
            
            with open(r'C:\Users\user\Desktop\Code\try_insta\idealofficial_followers.txt') as f:
                    followers = f.readlines()
                    followers = ([s.strip('\n') for s in followers ])
            new= set(followers_list) - set(followers)
            result1 = ''
            with open(r'C:\Users\user\Desktop\Code\try_insta\idealofficial_followers.txt', "a+") as f:
                f.write("\n")
                for item in new:
                    result1 = result1 + item + '\n'
                f.write(result1)
            with open(r'C:\Users\user\Desktop\Code\try_insta\idealofficial_followers.txt') as f:
                    final_followers = f.readlines()
                    final_followers = ([s.strip('\n') for s in final_followers ])
            if len(set(final_followers)) == followers_count:
                flag=False
    except:
        # insta_username = 'saba_insta5' #ban shode
        # insta_password = '123456Saba'
        # session = InstaPy(username=insta_username,
        #           password=insta_password,
        #           headless_browser=False)
        print('no')