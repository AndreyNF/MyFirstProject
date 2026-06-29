var getScreenApi = 'https://mini.s-shot.ru/1024x673/328/?';
var user_sites;
var index_mas;
var plus_btn;
var popular_sites_div;
var current_searcher = 'google';
var suggestions;

var searchEngines = {
    google: {
        search: {
            url: typeof Object.freeze !== "undefined" ? "s.html" : window.google_domain + "/search",
            value_name: "q"
        },
        'suggest': {
            url: "https://www.google.com/complete/search",
            value_name: "q",
            params: {
                "client": "chrome"
            },
            parse: function(json) {
                var suggests_array = [];

                json = json[1];
                for (var i = 0, l = json.length; i < l; i++)
                {
                    if (!(json[i] instanceof Array))
                    {
                        suggests_array.push({term: json[i]});
                    }
                }
                return suggests_array;
            }
        },
        class: "search-dropdown__ico_google"
    },
    mail: {
        search: {
            url: "https://go.mail.ru/search",
            value_name: "q",
            params: {
                "gp": "813092",
                "fr": "ps"
            }
        },
        class: "search-dropdown__ico_mail"
    },
    yandex: {
        search: {
            url: window.yandex_domain + "/search",
            value_name: "text",
            params: {},
        },
        suggest: {
            url: "https://suggest.yandex.ru/suggest-ya.cgi",
            value_name: "part",
            params: {
                "v": "4",
                "n": "10"
            },
            parse: function(json) {
                var suggests_array = [];

                json = json[1];
                for (var i = 0, l = json.length; i < l; i++)
                {
                    if (!(json[i] instanceof Array))
                    {
                        suggests_array.push({term: json[i]});
                    }
                }
                return suggests_array;
            }
        },
        class: "search-dropdown__ico_yandex"
    },
    bing: {
        search: {
            url: "https://www.bing.com/search",
            value_name: "q"
        },
        class: "search-dropdown__ico_bing"
    },
    yahoo: {
        search: {
            url: "https://www.my-search.com/search",
            value_name: "q",
            params: {
                "aid": "5156",
                "zoneid": "8260-1002"
            }
        },
        suggest: {
            url: "https://search.yahoo.com/sugg/gossip/gossip-us-ura",
            value_name: "command",
            params: {
                "output": "sd1",
                "nresults": "10"
            },
            parse: function(json) {
                var suggests_array = [];

                json = json['r'];
                for (var i = 0, l = json.length; i < l; i++)
                {
                    suggests_array.push({term: json[i]['k']});
                }
                return suggests_array;
            }
        },
        class: "search-dropdown__ico_yahoo"
    },
    rambler: {
        search: {
            url: "https://nova.rambler.ru/search",
            value_name: "query",
            params: {
                "_openstat": "bWFya2V0YXRvcjA3Ozs7"
            }
        },
        class: "search-dropdown__ico_rambler"
    },
    server_rules: {
        'search': {
            url: "/search/",
            value_name: "q",
        },
        'class': "search-dropdown__ico_server_rules"
    }
};
searchEngines.bing.suggest = searchEngines.yahoo.suggest;
searchEngines.mail.suggest = searchEngines.yandex.suggest;
searchEngines.rambler.suggest = searchEngines.yandex.suggest;
searchEngines.server_rules.suggest = searchEngines.google.suggest;

searchEngines.yahoo = searchEngines.google;
searchEngines.bing = searchEngines.google;
searchEngines.rambler = searchEngines.yandex;

function setTopWindowLocation(url, no_referer) {
    try {
        var targetWindow = window.top || window;
        if (no_referer && targetWindow.location && targetWindow.location.replace) {
            targetWindow.location.replace(url);
            return;
        }
        if (targetWindow.location) {
            targetWindow.location.href = url;
            return;
        }
    } catch (e) {}
    var link = document.createElement('a');
    link.href = url;
    link.target = '_top';
    if (no_referer) {
        link.rel = 'noreferrer';
        link.referrerPolicy = 'no-referrer';
    }
    document.body.appendChild(link);
    link.click();
    link.remove();
}

function trackOutboundLink(obj) {
    if ($(obj).parents('.hided').length)
    {
        return;
    }
    
    var url = obj.href;
    trackOutboundURL(url, function() {
        var target_attr = obj.getAttribute('target');
        switch (target_attr)
        {
            case '_blank':
                break;
            case '_top':
                setTopWindowLocation(url);
                break;
            default:
                document.location.href = url;
        }
    }, 'outbound_other');
    return obj.getAttribute('target') === '_blank';
}

function saveSites() {
    if (localStorage)
    {
        try
        {
            localStorage.setItem('user_sites', JSON.stringify(user_sites));
            localStorage.setItem('index_mas_' + _current_lang, JSON.stringify(index_mas));
        }
        catch (e) {}
    }
}

function getSites() {
    if (localStorage)
    {
        user_sites = localStorage.getItem('user_sites');
        if (user_sites)
        {
            user_sites = JSON.parse(user_sites);
        }
        index_mas = localStorage.getItem('index_mas_' + _current_lang);
        if (index_mas)
        {
            index_mas = JSON.parse(index_mas);
        }
    }
    
    if (!user_sites)
    {
        user_sites = {};
    }
    
    if (!index_mas)
    {
        index_mas = [];
        for (var i in user_sites)
        {
            index_mas.push(i);
        }
    }
    else
    {
        for (var i = 0; i < index_mas.length; i++)
        {
            var key = index_mas[i];
            if (!user_sites[key])
            {
                index_mas.removeElement(key);
            }
        }
        for (var i in user_sites)
        {
            if (index_mas.indexOf(i) < 0)
            {
                index_mas.push(i);
            }
        }
    }
}

function openUrl(url, inNewTab) {
    if (url.length > 1)
    {
        if (url.substr(0, 7) != 'http://' && url.substr(0, 8) != 'https://')
        {
            url = "http://" + url;
        }
        window.open(url, inNewTab ? '_blank' : '_self');
    }
}

function get_actual_search_engine(engine)
{
    var browser_lang = (navigator.language || navigator.systemLanguage || navigator.userLanguage).substr(0, 2).toLowerCase();
    result = engine;
    if (!/^(google|yandex|yahoo|mail)$/i.test(engine))
    {
        if (/^(ru|be|uk|ky|ab|mo|et|lv)$/i.test(browser_lang))
        {
            result = "yandex";
        }
        else
        {
            result = "yahoo";
        }
    }
    return result;
}

function setSearchEngine(name, do_not_save) {
    if (!name || !searchEngines[name])
    {
        return;
    }

    current_searcher = searchEngines[name];

    var form = $('#search_form');
    var input = $('#search_form .input');
    var add_options = form.find('.add_options');
    add_options && add_options.remove();
    
    if (current_searcher.search.params) 
    {
        var add_nodes = '<div class="add_options">';
        for (var key in current_searcher.search.params)
        {
            add_nodes += '<input type="hidden" name="' + key + '" value="' + current_searcher.search.params[key] + '">'
        }
        add_nodes += '</div>';
        form.append($(add_nodes));
    }

    form.attr('action', current_searcher.search.url);
    input.attr('name', current_searcher.search.value_name);
    // $('.search-dropdown__trigger span')[0].className = "search-dropdown__ico " + current_searcher.class;
    input.focus();

    if (localStorage && !do_not_save) 
    {
        localStorage.setItem('searchEngine', name);
    }
}

function freeSearchField() {
    suggestions && suggestions.hide();
    $('#search_form .input').focus();
}

function search(_this) {
    var search_str = $('#search_form .input').val();
    search_str = search_str.trim();
    var result = false;
    
    window.searchHistory && searchHistory.add(search_str);
    
    if ($('#search_form').hasClass('is_url'))
    {
        trackOutboundURL($('#search_form').attr('data_url'), function() {
            setTopWindowLocation($('#search_form').attr('data_url'), true);
        }, 'outbound_search');
        return false;
    }
    
    if (search_str)
    {
        setTimeout(function() {
            freeSearchField();
            suggestions.stop();
        }, 0);
        result = true;
    }
    else
    {
        result = false;
    }
    
    var query_string = $(_this).serialize();
    var searcher = _this.action;
    if (result && searcher && query_string)
    {
        var search_url_query = searcher + '?' + query_string;
        trackOutboundURL(search_url_query, function() {
            var target_attr = _this.getAttribute('target');
            switch (target_attr)
            {
                case '_blank':
                    break;
                case '_top':
                    setTopWindowLocation(search_url_query);
                    break;
                default:
                    document.location.href = search_url_query;
            }
        }, 'outbound_search');
        return _this.getAttribute('target') === '_blank';
    }
    
    return result;
}

function tryGetUrl(string) {
    string = string.trim();
    var resultURL = '';
    switch (string)
    {
        case 'youtube':
            resultURL = 'https://www.youtube.com/';
            break;
        case 'ютуб':
            resultURL = 'https://www.youtube.com/';
            break;
        case 'google':
            resultURL = window.google_domain + '/';
            break;
        case 'вк':
            resultURL = 'https://vk.com/';
            break;
        case 'facebook':
            resultURL = 'https://www.facebook.com/';
            break;
        case 'fb':
            resultURL = 'https://www.facebook.com/';
            break;
        case 'gmail':
            resultURL = 'https://mail.google.com';
            break;
        case 'яндекс':
            resultURL = window.yandex_domain + '/';
            break;
        default:
            var direct_link_from_map = window._query_direct_link_map[string.replace(' ', '+')];
            if (direct_link_from_map)
            {
                resultURL = direct_link_from_map;
            }
            else if (/(https?|ftp):\/\//.test(string))
            {
                resultURL = string.replace(' ', '%20');
            }
            else if (/^([а-яa-z0-9-_]+)(\.[а-яa-z0-9-_]+)*\.(biz|com|edu|gov|info|net|org|de|uk|cn|ru|eu|travel|club|рф|sc|pro|ua|by|kz)(\/[а-яa-z0-9-_]+)*(?:\/?)$/i.test(string) ||
                    /^((?:25[0-5]|2[0-4]\d|[01]?\d\d?)(\.(?=\d)|[\/:?#]|$)){4}/i.test(string))
            {
                resultURL = 'http://' + string;
            }
            break;
    }
    return resultURL;
}

function set_Data_URL_for_form_if_need(string) {
    var resultURL = tryGetUrl(string);
    
    if (resultURL)
    {
        $("#search_form").addClass('is_url');
        $("#search_form").attr('data_url', resultURL);
        return true;
    }
    else
    {
        $("#search_form").removeClass('is_url');
        $("#search_form").attr('data_url', '');
        return false;
    }
}

function toogleAddingTabPanel() {
    var plusTab = $(".preview-tab_new").toggleClass("preview-tab_new_active");
    $(".new-tab-adding").slideToggle();
    if (plusTab.hasClass("preview-tab_new_active"))
    {
        $('html, body').animate({
            scrollTop: $('.new-tab-adding').offset().top
        }, 400);
        $('.new-tab-adding__input-wrapper input').focus().val('');
        if (!$('.hided').length)
        {
            $('.popupar_heading').css('display', 'none');
        }
        else
        {
            $('.popupar_heading').css('display', '');
        }
    }
}

function init_suggestions() {
    var autocomplete_id = 0;
    var pause = false;
    var lastTerm = "";
    var curTerm = "";
    var current_suggestions = [];
    var last_loaded_web_suggestions = [];
    
    // Search
    var search_form = $("#search_form");
    var search_input = $("#search_form .input");
    var search_button = $("#search_form .search-bar__submit");
    var autocomplete = $("#autocomplete");
    
    function onSuggestionSelect(suggestion_dom) {
        search_form.removeAttr('autofill');
        var s1 = $(suggestion_dom).attr('data');
        set_Data_URL_for_form_if_need(s1);
        search_input.val(s1);
    }
    
    function show(suggests_array) {
        suggests_array.length && autocomplete.removeClass('hidden');
        for (var i = 0; i < suggests_array.length; i++)
        {
            var url = suggests_array[i].url || tryGetUrl(suggests_array[i].term);
            var s1text = suggests_array[i].term;
            var s2text = suggests_array[i].title || '';
            var suggest_dom = document.createElement('div');
            suggest_dom.className = 'autocomplete_element';
            suggest_dom.setAttribute('data', url || suggests_array[i].term);
            var s1text_dom = document.createElement('span');
            s1text_dom.className = 's1';
            s1text_dom.textContent = s1text;
            if (url)
            {
                s1text_dom.classList.add('link');
                var favicon = document.createElement('img');
                favicon.src = 'https://www.google.com/s2/favicons?domain=' + encodeURIComponent(url);
                suggest_dom.appendChild(favicon);
            }
            if (s2text)
            {
                var s2text_dom = document.createElement('span');
                s2text_dom.className = 's2';
                s2text_dom.textContent = s2text;
                var dash_dom = document.createElement('span');
                dash_dom.className = 'dash';
                dash_dom.textContent = '—';
                suggest_dom.appendChild(s2text_dom);
                suggest_dom.appendChild(dash_dom);
            }
            else
            {
                s1text_dom.classList.add('full');
            }
            suggest_dom.appendChild(s1text_dom);
            
            current_suggestions.push(suggests_array[i]);
            var auto = $(suggest_dom);
            autocomplete.append(auto);
            auto.on("click", function() {
                onSuggestionSelect(this);
                search_button.click();
            });
        }
    }
    
    function hide() {
        autocomplete.addClass('hidden');
        autocomplete.empty();
        autocomplete_id = 0;
        current_suggestions = [];
        curTerm = search_input.val();
    }
    
    function autoFill(suggestion) {
        var start_pos = search_input.val().length;
        var end_pos = suggestion.length;
        search_input.val(suggestion);
        
        if (search_input[0].setSelectionRange)
        {
            search_input[0].setSelectionRange(start_pos, end_pos, "backward");
        }
        else if (search_input[0].createTextRange)
        {
            var selRange = search_input[0].createTextRange();
            selRange.collapse(true);
            selRange.moveStart('character', start_pos);
            selRange.moveEnd('character', end_pos);
            selRange.select();
        }
        else if (typeof search_input[0].selectionStart)
        {
            search_input[0].selectionStart = start_pos;
            search_input[0].selectionEnd = end_pos;
        }
    }
    
    function findSuggestions(term) {
        search_form.removeAttr('autofill');
        if (lastTerm == term) 
        {
            return;
        }
        lastTerm = curTerm;
        hide();
        if (term !== '' && !pause)
        {
            curTerm = term;
        //    show([{term: term}]);
            
            var suggests_array = window.searchHistory ? searchHistory.getTop(term, 6) : [];
            var autofill_input;
            var autofill_attr;
            if (lastTerm.length < term.length && term.length > 4)
            {
                for (var i = 0; i < last_loaded_web_suggestions.length && suggests_array.length < 11; i++)
                {
                    if (last_loaded_web_suggestions[i].term.toLowerCase() != term.toLowerCase() &&
                        last_loaded_web_suggestions[i].term.toLowerCase().indexOf(term.toLowerCase()) >= 0 &&
                        (!window.searchHistory || !searchHistory.similarExists(suggests_array, last_loaded_web_suggestions[i]))) 
                    {
                        suggests_array.push(last_loaded_web_suggestions[i]);
                        if (!autofill_input && term.toLowerCase() != last_loaded_web_suggestions[i].term.toLowerCase() &&
                           last_loaded_web_suggestions[i].term.toLowerCase().indexOf(term.toLowerCase()) == 0)
                        {
                            autofill_input = last_loaded_web_suggestions[i].term;
                            autofill_attr = autofill_input;
                        }
                    }
                }
            }
            if (suggests_array && suggests_array.length)
            {
                var tmp_autofill_input = suggests_array[0].term || suggests_array[0].url;
                if (lastTerm.length < term.length && term != tmp_autofill_input && tmp_autofill_input.toLowerCase().indexOf(term.toLowerCase()) == 0)
                {
                    autofill_input = tmp_autofill_input;
                    autofill_attr = suggests_array[0].url || suggests_array[0].term;
                }
                if (autofill_input)
                {
                    autoFill(autofill_input);
                    search_form.attr('autofill', autofill_attr);
                }
                show(suggests_array);
            }

            var suggest_url = current_searcher.suggest.url + '?' + current_searcher.suggest.value_name + '=' + encodeURIComponent(term);
            for (var key in current_searcher.suggest.params)
            {
                suggest_url += '&' + key + '=' + current_searcher.suggest.params[key];
            }
            if (term.length > 1)
            {
                $.ajax({
                    url: suggest_url,
                    dataType: 'jsonp',
                    success: onloadSuggestions
                });
            }
        }
        else
        {
            hide();
        }
    }
    
    function onloadSuggestions(resp) {
        if (pause || !search_input.val())
        {
            return;
        }
        var suggests_array;
        try
        {
            suggests_array = current_searcher.suggest.parse(resp);
        }
        catch(e)
        {
            return;
        }
        
        if (suggests_array && suggests_array instanceof Array && suggests_array.length)
        {
            last_loaded_web_suggestions = suggests_array;
        }
    };

    search_input.on('focus', function() {
        pause = false;
    });
    
    var key_flag = false;
    search_input.on("keyup", function(e) {
        var keyCode = e.keyCode ? e.keyCode : e.which;
        switch (keyCode)
        {
            case 27: //Esc
                hide();
                search_input.val('');
                break;
                
            case 37:
                break;

            case 38:
                break;

            case 39:
                curTerm = search_input.val();
                break;

            case 40:
                break;

            case 13:
                break;
                
            case 16:
                break;
            case 17:
                break;
            case 18:
                break;
            case 20:
                break;
            case 91:
                break;

            default:
                key_flag && findSuggestions(this.value);
                break;
        }
        key_flag = false;
    });
    
    search_input.on("keydown", function(e) {
        key_flag = true;
        var keyCode = e.keyCode ? e.keyCode : e.which;
        switch (keyCode)
        {
            case 40:
                e.preventDefault();
                var childs = autocomplete.find('div');
                if (autocomplete_id < childs.length)
                {
                    autocomplete_id++;
                    var selected = autocomplete.find(".selected");
                    if (selected)
                    {
                        selected.removeClass("selected");
                    }
                    $(childs[autocomplete_id - 1]).addClass("selected");
                    onSuggestionSelect(childs[autocomplete_id - 1]);
                }
                break;
            case 38:
                e.preventDefault();
                var childs = autocomplete.find('div');
                if (autocomplete_id == 0) 
                {
                    autocomplete_id = childs.length + 1;
                }
                if (autocomplete_id > 1)
                {
                    autocomplete_id--;
                    var selected = autocomplete.find(".selected");
                    if (selected)
                    {
                        selected.removeClass("selected");
                    }
                    $(childs[autocomplete_id - 1]).addClass("selected");
                    onSuggestionSelect(childs[autocomplete_id - 1]);
                }
                break;
            default:
                break;
        }
    });
    
    return {
        stop: function() {
            pause = true;
        },
        hide: hide
    }
}

function createGridItem(site) {
    var isBrowser = /^(chrome:\/\/|edge:\/\/|secure:\/\/|about:)/.test(site.url);
    if (!site.title)
    {
        var url = site.url.match("^https?://([^:/\\?#]+)(?::[^/\\?#]+)?.*$");
        if (url && url[1])
        {
            site.title = url[1];
        }
        else
        {
            site.title = site.url;
        }
        saveSites();
    }
    if (!isBrowser && !site.icon)
    {
        var img = new Image();
        img.onload = function() {
            var favimg = $('.grid__item[x_url="' + site.url + '"]').find('.preview-tab__name-ico img');
            favimg.attr('src', img.src);
            site.icon = img.src;
            saveSites();
        };
        img.onerror = function() {
            img.src = 'https://www.google.com/s2/favicons?domain=' + site.title;
            site.icon = img.src;
            saveSites();
        }
        img.src = 'https://' + site.title + '/favicon.ico';
    }
    if (!isBrowser && !site.screen)
    {
        if (window.FileReader)
        {
            var xhr = getXMLHttpRequest();
            xhr.onload = function() {
                var reader = new FileReader();
                reader.onload = function(event) {
                    var dataUri = event.target.result;
                    var screenImg = $('.grid__item[x_url="' + site.url + '"] .preview-tab__picture-wrapper img');
                    screenImg.attr('src', dataUri);
                    site.screen = dataUri;
                    saveSites();
                };
                reader.onerror = function(event) {
                    var screenImg = $('.grid__item[x_url="' + site.url + '"] .preview-tab__picture-wrapper img');
                    screenImg.attr('src', getScreenApi + encodeURIComponent(site.url));
                };
                reader.readAsDataURL(this.response);
            }
            xhr.open('GET', getScreenApi + encodeURIComponent(site.url));
            xhr.responseType = 'blob';
            xhr.send();
        }
        else
        {
            site.screen = getScreenApi + encodeURIComponent(site.url);
        }
    }
    
    var addClass = '';
    if (site['class'])
    {
        addClass = site['class'];
    }
    return $('<div class="grid__item ' + addClass + '" x_url="' + site.url + '">\
                <div class="preview-tab">\
                  <div class="preview-tab__close">&times;</div>\
                  <a href="' + site.url + '" target="_top" onclick="return trackOutboundLink(this);" class="preview-tab__picture-wrapper">\
                    <div class="preview-tab__picture">\
                      <img src="' + site.screen + '" alt="">\
                    </div>\
                  </a>\
                  <div class="preview-tab__name">\
                    <div class="preview-tab__name-ico"><img src="' + site.icon + '" alt=""></div>\
                    <div class="preview-tab__name-text">' + site.title + '</div>\
                  </div>\
                </div>\
              </div>');
}

function getXMLHttpRequest() {
    if (window.XMLHttpRequest)
    {
        return new window.XMLHttpRequest;
    } 
    else
    {
        try
        {
            return new ActiveXObject("MSXML2.XMLHTTP.3.0");
        }
        catch (ex)
        {
            return null;
        }
    }
}

function onGridItemClick(event) {
    var _this = $(this).closest('.grid__item');
    if (_this.hasClass("hided"))
    {
        event.preventDefault();
        var url = _this.attr('x_url');
        _this.removeClass("hided");
        _this.insertBefore(plus_btn);

        index_mas.addElement(url);
        saveSites();
        
        toogleAddingTabPanel();
    }
}

function onGridItemClose(event) {
    var _this = $(this).closest('.grid__item');
    var url = _this.attr('x_url');
    event.preventDefault();

    if (!_this.hasClass('user'))
    {
        _this.addClass("hided");
        _this.appendTo(popular_sites_div);
    }
    else
    {
        _this.remove();
    }
    
    if (user_sites[url])
    {
        var site = user_sites[url];
        delete user_sites[url];
        index_mas.removeElement(url);
        saveSites();
    }
    
    
    
    if ($('.hided').length)
    {
        $('.popupar_heading').css('display', '');
    }
}

function updateSites() {
    $('#addedSites .grid__item:not(.addButton)').remove();
    
    for (var i = 0; i < index_mas.length; i++)
    {
        var key = index_mas[i];
        var site = user_sites[key];
        if (!site)
        {
            continue;
        }
        
        var grid = createGridItem(site);
        
        if (!site.hided)
        {
            grid.insertBefore(plus_btn);
        }
        else
        {
            grid.addClass('hided');
            grid.appendTo(popular_sites_div);
        }
        grid.on("click", '.preview-tab__close', onGridItemClose);
        grid.on("click", '.preview-tab__picture', onGridItemClick);
    }
}

function addNewSite(form) {
    var url = $(form).find('input').val().toLowerCase().trim();
    if (url)
    {
        if (!url.match(/^(http|https|chrome|about|edge|secure):.*/))
        {
            url = "http://" + url;
        }

        if (url[url.length - 1] == '/')
        {
            url = url.substr(0, url.length - 1);
        }

        var site = {};

        if (index_mas.indexOf(url) >= 0)
        {
            index_mas.removeElement(url);
        }
        if (user_sites[url])
        {
            site = user_sites[url];
            index_mas.addElement(url);
            var grid = $('.grid__item[x_url="' + site.url + '"]');
            grid.insertBefore(plus_btn);
        }
        else
        {
            site.url = url;
            site.screen = '';
            site.icon = '';
            site['class'] = 'user';
            user_sites[url] = site;
            index_mas.addElement(url);
            var grid = createGridItem(site);
            grid.addClass('user');
            grid.insertBefore(plus_btn).on("click", '.preview-tab__close', onGridItemClose);
        }

        saveSites();
        toogleAddingTabPanel();
    }
    
    return false;
}

function init_sites() {
    getSites();
    updateSites();
    freeSearchField();
}

$(document).ready(function() {
    $('.lang_selector').change(function() {
        var selected_lang = $(this).val();
        localize(selected_lang);
        init_sites();
    });
    
   /* $(".search-dropdown__trigger").click(function(event) {
        event.stopPropagation();
        $(".search-dropdown__list").toggleClass("search-dropdown__list_active");
        suggestions && suggestions.hide();
    });*/

    $(document).click(function(e) {
       /* if ($(".search-dropdown__list").hasClass('search-dropdown__list_active') && !$(e.target).is('.search-dropdown__list'))
        {
            $(".search-dropdown__list").removeClass("search-dropdown__list_active");
        }
        else */if (!$("#autocomplete").hasClass('hidden') && !$(e.target).is('.autocomplete_element'))
        {
            suggestions && suggestions.hide();
            $('#search_form .input').focus();
        }
    });

  /*  $(".search-dropdown__item").click(function() {
        setSearchEngine(this.innerText.trim().toLowerCase());
        $(".search-dropdown__list").removeClass("search-dropdown__list_active");
    });*/

    $(".new-tab-adding").hide();
    $(".preview-tab_new").click(function() {
        toogleAddingTabPanel();
    });
    
    $("#search_form").submit(function() {
        return search(this);
    });

    $(".new-tab-adding__form form").submit(function() {
        return addNewSite(this);
    });
    
    $('#search_form .input').keydown(function(e) {
        if (e.keyCode == 13)
        {
            set_Data_URL_for_form_if_need($('#search_form').attr('autofill') || this.value.trim());
        }
    });
    $('#search_form button').click(function() {
        set_Data_URL_for_form_if_need($('#search_form').attr('autofill') || $('#search_form .input').val().trim());
    });
    
    plus_btn = $(".grid__item.addButton");
    popular_sites_div = $("#popularSites");

    localize();
    setSearchEngine('server_rules', true);
    suggestions = init_suggestions();
    init_sites();
    window.scrollTo(0, 0);
});

function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

Array.prototype.removeElement = function(elem) {
    var ind = this.indexOf(elem);
    if (ind >= 0)
    {
        this.splice(ind, 1);
    }
};
Array.prototype.addElement = function(elem) {
    var ind = this.removeElement(elem);
    this.push(elem);
};
if (!Array.prototype.indexOf)
{
    Array.prototype.indexOf = function (elt, from) {
        var len = this.length >>> 0;
        var from = Number(arguments[1]) || 0;
        from = (from < 0) ? Math.ceil(from) : Math.floor(from);
        if (from < 0)
        {
            from += len;
        }

        for (; from < len; from++)
        {
            if (from in this && this[from] === elt)
            {
                return from;
            }
        }
        return -1;
    };
}
if (!String.prototype.trim)
{
    String.prototype.trim = function() {
        return this.replace(/^\s+|\s+$/g, ''); 
    }
}