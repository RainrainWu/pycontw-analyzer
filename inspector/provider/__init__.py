from inspector.extractor.attendee import Attendee_2019


class Provider():

    layer = 'provider'
    lake = {
        'attendee': Attendee_2019.export()
    }

    @classmethod
    def get_potential_sponsors_by_times(cls):

        roster = {}
        for attendee in cls.lake['attendee']:
            if attendee[2] not in roster:
                roster[attendee[2]] = 0
            roster[attendee[2]] += 1
        
        print(roster)

    @classmethod
    def get_potential_sponsors_by_level(cls):

        target_job = (
            'CTO', 'COO', 'CEO', 'CIO', 'CFO', 'CMO',
            'Co-founder', 'Founder'
        )
        roster = {}
        for attendee in cls.lake['attendee']:
            try:
                if any([x in attendee[3] for x in target_job]):
                    roster[attendee[2]] = attendee[3]
            except IndexError:
                continue

        print(roster)