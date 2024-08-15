tw = {'element': {'name': 'h3', 'class_': 'organization-portal__job-title'}}
ru = {'element': {'name': 'a', 'class_': 'opportunity-link break-word'}}
wa = {'element': {'name': 'div', 'class_': 'current-openings-details'}}
teams = {
    'Hawks': {
        'link': 'https://wd1.myworkdaysite.com/en-US/recruiting/hawks/External',
        'element': {'name': 'li', 'class_': 'css-1q2dra3'}
    },
    'Celtics': {
        'link': 'https://www.nba.com/celtics/careers',
        'element': {'name': 'a', 'class_': 'cursor-pointer'}
    },
    'Nets': {
        'link': 'https://www.bseglobal.net/careers/',
        'element': 'div.mb-6.md\\:mb-0.md\\:mr-6 h4'
    },
    'Hornets': {
        'link': 'https://recruiting.ultipro.com/HOR1011HORNT/JobBoard/5b257d2d-0813-4167-b64c'
                '-95fb001e0d96/?q=&o=postedDateDesc',
        **ru
    },
    'Bulls': {
        'link': 'https://www.nba.com/bulls/career-opportunities',
        'element': {'name': 'div', 'class_': 'gnewtonCareerGroupJobTitleClass'}},
    'Cavaliers': {
        'link':
            'https://www.teamworkonline.com/basketball-jobs/cleveland-cavaliers/cleveland'
            '-cavaliers-jobs',
        **tw
    },
    'Mavericks': {
        'link': 'https://recruitingbypaycor.com/career/CareerHome.action?clientId'
                '=8a7883c68eee9454018ef2f81a7d05a4',
        'element': {'name': 'div', 'class_': 'gnewtonCareerGroupJobTitleClass'}
    },
    'Nuggets': {
        'link': 'https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid'
                '=458d5dd5-1f4f-46b7-8920-ec4bbbdb1d10&ccId=19000101_000001&type=JS&lang=en_US',
        **wa
    },
    'Pistons': {
        'link': 'https://www.teamworkonline.com/basketball-jobs/palacenet/detroit-pistons-jobs-',
        'element': {'name': 'h3', 'class_': 'organization-portal__job-title'}
    },
    'Warriors': {
        'link': 'https://www.teamworkonline.com/basketball-jobs/warriors/golden-state-warriors'
                '-careers',
        **tw
    },
    'Rockets': {
        'link': 'https://www.teamworkonline.com/basketball-jobs/houston-rockets-jobs/houston'
                '-rockets',
        **tw
    },
    'Lakers': {
        'link': 'https://www.teamworkonline.com/basketball-jobs/los-angeles-lakers/los-angeles'
                '-lakers-jobs',
        **tw
    },
    'Kings': {
        'link': 'https://www.teamworkonline.com/basketball-jobs/sacramento-kings-jobs/sacramento'
                '-kings',
        **tw
    },
    'Wizards': {
        'link': 'https://www.teamworkonline.com/multiple-properties/monumentalsports/monumental'
                '-sports',
        **tw
    },
    'Jazz': {
        'link': 'https://www.teamworkonline.com/basketball-jobs/utah-jazz-jobs/utah-jazz',
        **tw
    },
    'Heat': {
        'link': 'https://recruiting.ultipro.com/MIA1004MHLP/JobBoard/b34868a3-6ce1-4a28-b8fb'
                '-afb1cd5be9d3/?q=&o=postedDateDesc',
        **ru},
    'Suns': {
        'link': 'https://recruiting2.ultipro.com/PHO1000PHXSE/JobBoard/c249bb71-c106-49f4-9ae1'
                '-fd8f0173d326/?q=&o=postedDateDesc',
        **ru},
    'Magic': {
        'link': 'https://recruiting.ultipro.com/ORL1001MAGIC/JobBoard/d2d331e7-e222-4a47-bb35'
                '-c640aa29a3d7/?q=&o=postedDateDesc',
        **ru},
    'Bucks': {
        'link': 'https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid'
                '=035c77cb-5b5c-4e48-b858-605ab1663076&ccId=19000101_000001&type=JS&lang=en_US',
        **wa
    },
    'Pacers': {
        'link': 'https://pse.hrmdirect.com/employment/job-openings.php?search=true&',
        'element': {'name': 'td', 'class_': 'posTitle'}
    },
    'Clippers': {
        'link': 'https://www.nba.com/clippers/company/careers/openpositions',
        'element': {'name': 'h3', 'class_': 'text-blue hover:text-red'}
    },
    'Grizzlies': {
        'link': 'https://careers-grizzlies.icims.com/jobs/search?mobile=false&width=1200&height'
                '=500&bga=true&needsRedirect=false&jan1offset=-420&jun1offset=-420',
        'element': {'name': 'div', 'class_': 'container-fluid iCIMS_JobsTable'}
    },
    'Timberwolves': {
        'link': 'https://jobs.dayforcehcm.com/en-US/packportal/CANDIDATEPORTAL',
        'element': {'element': {'name': 'h2', 'class_': 'css-njwewr'}}
    },
    'Spurs': {
        'link': 'https://jobs.dayforcehcm.com/en-US/onesse/CANDIDATEPORTAL',
        'element': {'name': 'h2', 'class_': 'css-1w2qp4v'}
    },
    'Pelicans': {
        'link': 'https://us241.dayforcehcm.com/CandidatePortal/en-US/bensonenterprises/SITE'
                '/SAINTSPELSCAREERS',
        'element': {'name': 'div', 'class_': 'posting-title'}
    },
    'Knicks': {
        'link': 'https://www.msgsports.com/jobs/?departments=&locations=',
        'element': {'name': 'div', 'class_': 'job-entry__col--title'}
    },
    'Thunder': {
        'link': 'https://www.nba.com/thunder/employment',
        'element': {'name': 'p', 'class_': 'has-text-align-center'}
    },
    '76ers': {
        'link': 'https://recruit.hirebridge.com/v3/CareerCenter/v2/?cid=8097',
        'element': {'name': 'span', 'class_': 'title'}
    },
    'Trail Blazers': {
        'link': 'https://jobs.ripcity.org/search/jobs?q=',
        'element': {'name': 'h2', 'class_': 'space-none'}
    },
    'Raptors': {
        'link': 'https://careers.smartrecruiters.com/MLSE3',
        'element': {'name': 'h4', 'class_': 'link--block-target'}
    }

}

just_text = ['Nets', 'Hornets', 'Cavaliers', 'Pistons', 'Warriors', 'Rockets', 'Lakers', 'Kings',
             'Wizards', 'Jazz', 'Heat', 'Suns', 'Magic', 'Pacers', 'Clippers', 'Timberwolves',
             'Thunder', '76ers', 'Raptors']

strip_text = ['Celtics', 'Mavericks', 'Pelicans', 'Trail Blazers']

scroll = ['Nuggets', 'Bucks']

ss = ['Bulls']

iframes = ['Grizzlies', ]
