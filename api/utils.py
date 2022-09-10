def obj_to_post(obj):
    """
    obj 의 각 속성을 serialize 해서, dict 로 변환한다.
    serialize: python object --> (기본타입) int, float, str
    :param obj:
    :return:
    """
    post = dict(vars(obj))

    if obj.category:
        post["category"] = obj.category.name
    else:
        post["category"] = "NoCategory"

    if obj.tags:
        post["tags"] = [t.name for t in obj.tags.all()]
    else:
        post["tags"] = []

    if obj.image:
        post["image"] = obj.image.url
    else:
        post["image"] = "https://via.plateholder.com/900x400/"

    if obj.update_dt:
        post["update_dt"] = obj.update_dt.strftime("%Y-%m-%d %H:%M:%S")
    else:
        post["update_dt"] = "9999-12-31 00:00:00"

    del post["_state"], post["category_id"], post["create_dt"]

    return post
