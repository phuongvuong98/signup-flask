/**
 * Created by Phuong Vuong on 5/11/2019.
 */
function FBlogin() {
    FB.login(function (responseLogin) {
        FB.api('/me', {fields: 'name, email'}, function (responseInfo) {
            console.log(responseInfo);
            var obj = {
                id_fb: responseLogin.authResponse.userID,
                email_fb: responseInfo.email
            };
            var data_json = JSON.stringify(obj);
            $.ajax({
                url: "/api/fb/register",
                type: "POST",
                data: data_json,
                dataType: "json",
                async: false,
                contentType: "application/json",
                success: function (data, textStatus, jqXHR) {
                    if (data == true) {
                        // location.replace("/welcome");
                        alert("Sign up successful")
                    } else alert("Sign up facebook fail")
                }
            });
        });
    }, {
        scope: "public_profile,email",
        return_scopes: true
    });
}

function fetchUserDetail() {
    FB.api('/me', {fields: 'name, email'}, function (response) {
        console.log('Successful login for: ' + response.name + " " + response.email + " " + response.id);
    });
}

function checkFBlogin() {
    FB.getLoginStatus(function (response) {
        // if (response.status === 'connected') {
        //     fetchUserDetail();
        // } else if (response.status === 'not_authorized') {
        //     FBlogin();
        //     console.log("Please log into this app.")
        // } else {
        //     FBlogin();
        //     console.log("Please log into this Facebook.")
        // }
        FBlogin();
        console.log("Sign up with fb.")
    });
}