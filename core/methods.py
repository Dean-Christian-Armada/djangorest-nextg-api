# Standard API Envelope
def standardResponse(data=[], errors=[], **kwargs):
    return {"data":data, "errors":errors}

# for dynamic folder name of school
def school_logo_upload_path_handler(instance, filename):
	name = instance.name.lower().replace(" ", "-")
	return "schools/{school}/logo.png".format(school=name)

def group_picture_upload_path_handler(instance, filename):
	school = instance.created_by.school.name.lower().replace(" ", "-")
	group = instance.name.lower().replace(" ", "-")
	return "schools/{school}/{group}/picture.png".format(school=school, group=group)