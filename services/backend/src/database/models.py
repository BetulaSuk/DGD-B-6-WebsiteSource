from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Notes(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    author = fields.ForeignKeyField("models.Users", related_name="note")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author} on {self.created_at}"


class PdfData(models.Model):
    paper_id = fields.CharField(max_length=255,
                                pk=True,
                                unique=True,
                                index=True,
                                null=False)
    title = fields.TextField(null=False)
    abstract = fields.TextField(null=True)
    author = fields.TextField(null=True)
    date = fields.DatetimeField(null=False)
    conference = fields.CharField(max_length=255, null=True)
    year = fields.IntField(null=True)
    link = fields.CharField(max_length=255, null=True)
    update_time = fields.DatetimeField(null=True)
    journal = fields.CharField(max_length=255, index=True, null=True)
    issn = fields.CharField(max_length=255, null=True)
    first_page = fields.IntField(null=True)
    last_page = fields.IntField(null=True)
    publisher = fields.CharField(max_length=255, null=True)
    doi = fields.CharField(max_length=255, null=True)
    keywords = fields.CharField(max_length=255, null=True)


class ArxivData(models.Model):
    paper_id = fields.CharField(max_length=255,
                                pk=True,
                                unique=True,
                                index=True,
                                null=False)
    title = fields.TextField(null=False)
    author = fields.TextField(null=True)
    link = fields.CharField(max_length=255, null=True)
    abstract = fields.TextField(null=True)
    keywords = fields.CharField(max_length=255, null=True)
    last_submit_time = fields.TextField(null=True)
