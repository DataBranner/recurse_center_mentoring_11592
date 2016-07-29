import pickle
import pprint
import datetime

def unpickleuser():
    userjson = pickle.load(open('randuser.json', 'rb'))
    pp = pprint.PrettyPrinter()
    pp.pprint(userjson)
    return userjson

def unpicklerepo():
    repojson = pickle.load(open('randrepo.json', 'rb'))
    return repojson



class Analysis():
    def __init__(self):
        self.data = unpickleuser()

    def followers(self):
        followercount = []
        for follower in self.data:
            followercount.append(follower.get('followers'))
        print(followercount)
        return followercount

    def following(self):
        followingcount = []
        for following in self.data:
            followingcount.append(following.get('following'))
        print(followingcount)
        return followingcount

    def publicgists(self):
        publicgistscount = []
        for publicgists in self.data:
            publicgistscount.append(publicgists.get('public_gists'))
        print(publicgistscount)
        return publicgistscount

    def publicrepos(self):
        publicreposcount = []
        for publicrepos in self.data:
            publicreposcount.append(publicrepos.get('public_repos'))
        print(publicreposcount)
        return publicreposcount

    def createdat(self):
        """return timeedelta since the account was created"""
        createdatcount = []
        for createdat in self.data:
            pycreatedat = datetime.datetime.strptime(createdat.get('created_at'), "%Y-%m-%dT%H:%M:%SZ")
            createddelta = datetime.datetime.now() - pycreatedat
            createdatcount.append(createddelta)
        print(createdatcount)
        return createdatcount

    def getghindex(self, user):
        # get the stargazers counts from the json
        for user in repojson:
            for repo in user:
                for k, v in repo.iteritems():
                    if k == "stargazers_count" and v != 0:
                        repolist.append(v)

        # sometimes there are no stars :(
        if repolist == []:
            return jsonify(result="No stars found.")
        else:
            sortedlist = sorted(repolist)

            # calculate the h-index
            for item in sortedlist:
                remaininglist = len(sortedlist[sortedlist.index(item):])
                if remaininglist > item:
                    countlist.append(item)
                elif remaininglist == item:
                    countlist.append(item)
                    break
                else:
                    while remaininglist < item:
                        item -= 1
                    else:
                        countlist.append(item)
                        break
            return jsonify(result=str(max(countlist)))



unpickleuser()
unpicklerepo()
analyze()
