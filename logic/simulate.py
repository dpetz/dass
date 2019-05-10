"""..."""

from logic.states import init, progress, absorbing, verify_states
from logic.ads import verify_ads, eligible_in_state
from util.validate import verify, seq, prob
from util.stats import describe



def sample_impressibilites(impress,n):
    """dictionary of functions for each ad that will sample impressibility for given user numbers"""
    imp = {ad: f(n) for ad, f in impress.items()}
    verify(seq(seq(prob)), list(imp.values()))
    return imp


def streams(states, ads, impress, n=10):
    """Generate n streams based on states
    :param states: dictionary as defined verify_states
    :param ads: dictionary as defined in verify_ads
    :param impress: input function for sample_impressibilites
    :param n: number of streams"""

    verify_states(states)
    verify_ads(ads)

    # impressibility per ad per user
    impress_ad_user = sample_impressibilites(impress, n)

    absorbing_states = absorbing(states)
    streams_all_users = []
    views_all_users = []

    for user in range(n):
        state = init(states)  # current state
        stream = [state]      # names of states user traverses
        views = []            # ad views as (ad,index)
        i = 0
        while state not in absorbing_states:

            # pick first ad eligible in current state
            ad_options = eligible_in_state(ads, states['names'][state])
            if ad_options:
                ad = ad_options[0]
                ad_name = ads['names'][ad]

                # If user targeted by ad type?"
                # print(ad, user, impress_ad_user)
                if impress_ad_user[ad_name][user] >= ads['min_impress'][ad]:
                    views.append((ad_name, i))

            state = progress(state,states)
            stream.append(state)

            i += 1

        streams_all_users.append(stream)
        views_all_users.append(views)

    views_stats = describe(list(map(len, views_all_users)))

    return {
        'stats': {'users': n, 'views': views_stats},
        'streams': streams_all_users,
        'views': views_all_users,
        'impressibilities': impress_ad_user
    }


