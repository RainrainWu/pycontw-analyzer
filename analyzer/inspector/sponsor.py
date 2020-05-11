from analyzer import provider

def filter_potential_sponsor_by_time(threshhold):

    roster = {}
    deprecated_flag = [
        'School', 'school',
        'University', 'university',
        '國中', '高中', '大學', '研究所'
    ]
    
    company_times = provider.get_attendee_companies_with_times()
    for company in company_times:
        if all([(x not in company) for x in deprecated_flag]) and \
                int(company_times[company]) > threshhold:
            roster[company] = company_times[company]
    
    for i in roster:
        print('{COMPANY} {TIMES}'.format(COMPANY=i, TIMES=roster[i]))

def filter_potential_sponsor_by_level():

    roster = {}
    target_job = (
        'CTO', 'COO', 'CEO', 'CIO', 'CFO', 'CMO', 'CCO'
        'Co-founder', 'Founder'
    )

    company_jobs = provider.get_attendee_companies_with_jobs()
    for company in company_jobs:
        if any([x in company_jobs[company] for x in target_job]):
            roster[company] = company_jobs[company]

    for i in roster:
        print('{COMPANY} {JOBS}'.format(COMPANY=i, JOBS=roster[i]))
