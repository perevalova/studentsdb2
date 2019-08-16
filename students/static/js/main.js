function initTabLoad() {
    $('.ajax-load').click(function(event) {
        var tab = $(this);
        var toLoad = tab.children('a').attr('href');
        var content = $('#content-columns');

        content.fadeOut(400, loadContent); // hide content
        history.pushState(null, '', toLoad); //change URL
        function loadContent() {
            content.load(toLoad + ' #content-column', '');
            // content.show('speed'); // show new content
            content.fadeIn(); // show new content
        }
        // function showNewContent() {
        //     content.show('speed'); // show new content
        // }

        if (!tab.hasClass('active')) {
            $('.nav li').removeClass('active');
            tab.addClass('active');
        }

        return false;

    });
}

function initAddTabClass() {
    // add class="active" to selected tab in navigation tabs
    if (window.location.pathname.indexOf("/") == 0) {
            $('.nav li').removeClass('active');
            $('.nav li:eq(0)').addClass('active');
        }
    if (window.location.href.indexOf("journal") > -1) {
            $('.nav li').removeClass('active');
            $('.nav li:eq(1)').addClass('active');
        }
    if (window.location.href.indexOf("groups") > -1) {
            $('.nav li').removeClass('active');
            $('.nav li:eq(2)').addClass('active');
        }
    if (window.location.href.indexOf("exams") > -1) {
            $('.nav li').removeClass('active');
            $('.nav li:eq(3)').addClass('active');
        }
    if (window.location.href.indexOf("contact-admin") > -1) {
            $('.nav li').removeClass('active');
            $('.nav li:eq(4)').addClass('active');
        }
    if (window.location.href.indexOf("users") > -1) {
            $('.nav li').removeClass('active');
            $('.nav li:eq(5)').addClass('active');
        }
    if (window.location.href.indexOf("accounts") > -1) {
            $('.nav li').removeClass('active');
        }

}

function initPagination() {
    $('.pagin').click(function(event) {
        var toLoad = $(this).attr('href');
        var pageselect = $('.table');

        // change pagination tabs
        // content.hide('100', loadContent); // hide content
        history.pushState(null, '', toLoad); //change URL

        // update table
        pageselect.fadeOut(400, loadContent); // hide content
        function loadContent() {
            pageselect.load(window.location.href + ' .table', '');
            pageselect.append(window.location.href + ' .table', '');
            pageselect.fadeIn();
        }

        if ($('.pagination li').hasClass('active')) {
            $('.pagination li').removeClass('active');
            $(this).parent('li').addClass('active');
        }
        return false;

    });
}


function initGroupSelector() {
    // look up select element with groups and attach our even handler on field "change" event
    $('#group-selector select').change(function(event){
        // get value of currently selected group option
        var group = $(this).val();
        var groupselector = $('.table');

        if (group) {
            // set cookie with expiration date 1 year since now;
            // cookie creation function takes period in days
            $.cookie('current_group', group, {'path': '/', 'expires': 365});
        } else {
            // otherwise we delete the cookie
            $.removeCookie('current_group', {'path': '/'});
        }

        // ajax update info table
        groupselector.fadeOut(400, loadContent); // hide content
        function loadContent() {
            groupselector.load(window.location.href + ' .table', '', showNewContent);
        }
        function showNewContent() {
            groupselector.fadeIn(400); // show new content
        }

        // and reload a page
        location.reload(true);

        return true;
    });
}


function initJournal() {
    var indicator = $('#ajax-progress-indicator');
    var errormessage = $('#error_message');

    $('.day-box input:checkbox').click(function(event){
        var box = $(this);
        $.ajax(box.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'pk': box.data('student-id'),
                'date': box.data('date'),
                'present': box.is(':checked') ? '1' : '',
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'beforeSend': function(xhr, settings){
                indicator.show();
            },
            'error': function(xhr, status, error){
                errormessage.show();
                // alert(data.status);
                indicator.hide();
            },
            'success': function(data, status, xhr){
                indicator.hide();
            }
        });
    });
}

function initDateFields() {
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD',
        'locale': 'uk'
    }).on('dp.hide', function(event){
        $(this).blur();
    });
}

$(function () {
// function initEditPage() {
    var indicator = $('#progress-spinner');

    $('#content-column').on('click', '.edit-form-link', function(event){
        var link = $(this);
        var url = $('a.edit-form-link');
        $.ajax({
            'url': url.attr('href'),
            'dataType': 'html',
            'type': 'GET',
            'success': function(data, status, xhr){
                // check if we got successfull response from the server
                if (status !== 'success') {
                    alert(gettext('There was an error on the server. Please, try again a bit later.'));
                    return false;
                }

                // update modal window with arrived content from the server
                var modal = $('#myModal'), html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                modal.find('.modal-body').html(form);

                // init our edit form
                initEditForm(form, modal);

                // setup and show modal window finally
                modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true
                });
                indicator.hide();
            },
            'beforeSend': function(xhr, settings){
                indicator.show();
                link.click(function(event) {
	                return false;
                })
            },
            'error': function(){
                alert(gettext('There was an error on the server. Please, try again a bit later.'));
                return false;
                indicator.hide();
            }
        });

        return false;
    });
});

function initEditForm(form, modal) {
    // attach datepicker
    initDateFields();

    // close modal window on Cancel button click
    form.find('input[name="cancel_button"]').on('click', function(event){
        modal.find('.modal-body').html(html.find('.alert'));
        setTimeout(function(){location.reload(true);}, 500);
        return false;
    });

    // make form work in AJAX mode
    form.ajaxForm({
        'dataType': 'html',
        'error': function() {
            alert(gettext('There was an error on the server. Please, try again a bit later.'));
            return false;
        },
        'success': function(data, status, xhr) {
            var html = $(data), newform = html.find('#content-column form');

            // copy alert to modal window
            modal.find('.modal-body').html(html.find('.alert'));

            // copy form to modal if we found it in server response
            if (newform.lenght > 0) {
                modal.find('.modal-body').append(newform);

                // initialize form fields and buttons
                initEditForm(newform, modal);
            } else {
                // if no form, it means success and we need to reload page to get updated students list;
                // reload after 2 seconds, so that user can read success message
                // TODO: ajax update info
                //html.load('home');
                setTimeout(function(){location.load('home .table');}, 500);
            }
             setTimeout(function(){location.load('home .table');}, 500);

        },
        'beforeSand': function () {
            html.find('input, textarea').attr({readonly, disabled});
            modal.find('.modal-body').html('<div class="alert alert-warning" role="alert">Відправка форми...</div>');
        }
    });
}

$(function () {
// function initAddPage() {
    var indicator = $('#progress-spinner');

    $('#content-column').on('click', '.add-form-link', function(event){
        var link = $(this);
        var url = $('a.add-form-link');
        $.ajax({
            'url': url.attr('href'),
            'dataType': 'html',
            'type': 'GET',
            'success': function(data, status, xhr){
                // check if we got successfull response from the server
                if (status !== 'success') {
                    alert(gettext('There was an error on the server. Please, try again a bit later.'));
                    return false;
                }

                // update modal window with arrived content from the server
                var modal = $('#myModal'), html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                modal.find('.modal-body').html(form);

                // init our edit form
                initAddForm(form, modal);

                // setup and show modal window finally
                modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true
                });
                indicator.hide();
            },
            'beforeSend': function(xhr, settings){
                indicator.show();
                link.click(function(event) {
	                return false;
                })
            },
            'error': function(){
                alert(gettext('There was an error on the server. Please, try again a bit later.'));
                return false;
                indicator.hide();
            }
        });

        return false;
    });
});

function initAddForm(form, modal) {
    // attach datepicker
    initDateFields();

    // close modal window on Cancel button click
    form.find('input[name="cancel_button"]').on('click', function(event){
        modal.find('.modal-body').html(html.find('.alert'));
        setTimeout(function(){location.reload(true);}, 500);
        return false;
    });

    // make form work in AJAX mode
    form.ajaxForm({
        'dataType': 'html',
        'error': function() {
            alert(gettext('There was an error on the server. Please, try again a bit later.'));
            return false;
        },
        'success': function(data, status, xhr) {
            var html = $(data), newform = html.find('#content-column form');

            // copy alert to modal window
            modal.find('.modal-body').html(html.find('.alert'));

            // copy form to modal if we found it in server response
            if (newform.lenght > 0) {
                modal.find('.modal-body').append(newform);

                // initialize form fields and buttons
                initAddForm(newform, modal);
            } else {
                // if no form, it means success and we need to reload page to get updated students list;
                // reload after 2 seconds, so that user can read success message
                // TODO: ajax update info
                //html.load('home');
                setTimeout(function(){location.load('home .table');}, 500);
            }
             setTimeout(function(){location.load('home .table');}, 500);

        },
        'beforeSand': function () {
            html.find('input, textarea').attr({readonly, disabled});
            modal.find('.modal-body').html('<div class="alert alert-warning" role="alert">Відправка форми...</div>');
        }
    });
}


$(document).ready(function(){
    initPagination();
    initTabLoad();
    initAddTabClass();
    initJournal();
    initGroupSelector();
    initDateFields();
    // initEditPage();
    initEditForm();
    // initAddPage();
    initAddForm();
});
