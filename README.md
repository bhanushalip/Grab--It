# Grab-it!
A small luck-based game built during CSI-RAIT's Web Development Workshop using [Django Web Framework](https://www.djangoproject.com/)

## Quiz Links
1 - [Basics](http://bit.ly/csi-webdev-1)
2 - [Web Architecture](http://bit.ly/2mnWqoc)
3 - [Web Technologies](http://bit.ly/csi-webdev-3)

## Quick Access 

### Front-end

**HTML BASE EXTEND TEMPLATE**

```
{% extends 'base.html' %}
{% load static %}
{% block content %}
 <!-- HTML CONTENT GOES HERE -->


{% endblock %}
```

**Column HTML**
```
<div id="box-items" class="container">
        <div class="row">
            {% for item in response.items %}
            <div class="col-sm-3">
                <div class="card">
                    <img class="card-img-top" src="media/{{item.img}}" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title">{{item.title}}</h5>
                        <p class="card-text">{{item.description}}</p>
                        <a site="{% url 'grab' item_id=item.uuid %}" data-toggle="modal" data-target="#exampleModalCenter" class="grab btn btn-danger text-white">Grab this!</a>
                    </div>  
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
```

**Style References**
```
FINAL STYLES 
body{
    background-color:#e9ecef;
}

#thor-image{
    height: 300px;
}

#thor-proud{
    height: 350px;
}
#thor-image{
    height: 300px;
}
.subtitle{
    font-size:2em;
}

#box-items{
    padding:20px;
}

.card{
    margin:10px;
}
```

**Flex Box**
```
d-flex justify-content-center align-items-center
```

**Jumbotron Class**
```
jumbotron jumbotron-fluid
```

### Back-end

**Item Model**
```
class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    is_worthy = models.BooleanField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title
```

**Admin Item Model**
```
@admin.register(Item)
class Item(admin.ModelAdmin):
    fields = ('title', 'description', 'img', 'is_worthy')
    list_display = ('title', 'description', 'is_worthy')
```


**Modal Code**
    <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                
                <div class="modal-body">
                        <div class="text-center">
                                <div class="spinner-border" role="status">
                                  <span class="sr-only">Loading...</span>
                                </div>
                                <h3><span class="text-danger">Thor </span>is calculating your worth... </h3>
                              </div>
                </div>
              </div>
            </div>
          </div>
