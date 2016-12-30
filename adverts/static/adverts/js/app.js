// documen ready
jQuery(document).ready(function () {
    if (!localStorage.data){
        var data = [];
        localStorage.data = JSON.stringify(data);
    }
});

jQuery(document).ready(function () {
    var adverts_div = jQuery('#adverts');

    jQuery(adverts_div).click(function (event) {
        var target = event.target;
        if (target.tagName == 'A'){
            update_url(target);
        }
    });
});


// update url and update db
var get_id = function (href) {
    var split_url = href.split('/')
    var id = Number((split_url[split_url.length - 1]));
    return id;
};

var update_url = function (target) {
    var id = get_id(target.href);

    if (id in get_data()){
        target.href += '?v=1';
    } else {
        update_data(id);
        target.href += '?v=0';
    }
};


// db
function get_data () {
    return JSON.parse(localStorage.data);
}

function update_data(id) {
    var data = JSON.parse(localStorage.data);
    data.push(id)
    if (id in data)
        return ;
    console.log(data);
    localStorage.data = JSON.stringify(data);
}
