

class Constant:

    GENDER_MAIL = 'male'
    GENDER_FEMAIL = 'female'
    GENDER_NOT = 'not-specified'

    GENDER_CHOICES = (
        (GENDER_MAIL, 'Male'),
        (GENDER_FEMAIL, 'Female'),
        (GENDER_NOT, 'Not specified')
    )

    TYPE_LIKE = 'like'
    TYPE_COMMENT = 'comment'
    TYPE_FOLLOW = 'follow'

    TYPE_CHOICES = (
        (TYPE_LIKE, 'Like'),
        (TYPE_COMMENT, 'Comment'),
        (TYPE_FOLLOW, 'Follow'),
    )
