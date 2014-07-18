<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>IPNB Session $$SESSNAME</title>

    <link rel="stylesheet" type="text/css" href="//code.jquery.com/ui/1.11.0/themes/smoothness/jquery-ui.css" />
    <link rel="stylesheet" type="text/css" href="/jdock_assets/css/base.css" />
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="//code.jquery.com/ui/1.11.0/jquery-ui.min.js"></script>
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

    <script>
        $(function() {
            $( "#tabs" ).tabs();
        });
    </script>
</head>
<body>

<div class="container">
    <div class="navbar-header">
        <img class="navbar-brand" src="/jdock_assets/img/juliacloudlogo.png" height="25px"></img>
        <span class="navbar-brand">JuliaBox</span>
    </div>
    <div class="col-md-9">
        <ul class="nav nav-pills" role="tablist">
            <li class="active"><a href="#ijulia" data-toggle="tab">IJulia</a></li>
            <li><a href="#console" data-toggle="tab">Console</a></li>
            <li><a href="#fileman" data-toggle="tab">File Manager</a></li>
            <li><a href="#admin" data-toggle="tab">Admin</a></li>
        </ul>
    </div>
    <div style="clear:both;"></div>
 
    <div id="tabs" class="tab-content modules">
        <div id="ijulia" class="tab-pane active">
            <iframe id="ijulia_iframe" src="/hostipnbsession/" frameborder="0" width="100%" height="90%"></iframe>  
        </div>
        <div id="console" class="tab-pane fade">
            This is a bash session. If you cannot see a blinking cursor below, please right-click, "reset" the terminal and hit "enter". <br/>
            Type "julia" to start a Julia REPL session.<br/><br/>
            
            <iframe id="console_iframe" src="/hostipnbupl/shellinabox" frameborder="0" width="100%" height="90%"></iframe>  
        </div>
        <div id="fileman" class="tab-pane fade">
            <iframe id="fileman_iframe" src="/hostipnbupl/" frameborder="0" width="100%" height="90%"></iframe>  
        </div>
        <div id="admin" class="tab-pane fade">
            <iframe id="admin_iframe" src="/hostadmin/" frameborder="0" width="100%" height="90%"></iframe>  
        </div>
    </div>
</div> <!-- container -->
 
</body>
</html>



