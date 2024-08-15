import db_fns as db
from teams import just_text, strip_text


def parse(jobs, team):
    new_jobs = []
    cj = db.select(team)
    curr_jobs = [c[0] for c in cj]
    # set all active jobs to not active
    for job in jobs:
        if team == 'Thunder':
            if job.get_text() == 'PART-TIME JOBS':
                break

        j = team_parse(job, team)
        if j != '' and j not in curr_jobs and j is not None:
            new_jobs.append((j, team))
        else:
            # set active - true
            pass
    db.insert(new_jobs)
    return new_jobs


def team_parse(job, team):
    if team == 'Hawks':
        return job.get_text().split('locations')[0]
    if team in strip_text:
        return job.get_text().strip()
    if team in just_text:
        return job.get_text()
    if team == 'Bulls':
        return job.split(' Chicago, IL')[0]
    if team == 'Nuggets':
        return city_split('Denver, CO', job.get_text(),'DEN')
    if team == 'Bucks':
        return city_split('Milwaukee, WI', job.get_text(), 'MIL')
    if team == 'Grizzlies':
        return job.text.split("\n")[1]
    if team == 'Knicks':
        return job.get_text().strip().split("\n")[0].strip()


def city_split(city, job, abbrev):
    if city in job:
        return job.split(f' {city}')[0]
    return f'NON-{abbrev}'
