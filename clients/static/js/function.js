var app = angular.module("app", []);

app.controller("AppCtrl", function($http) {
    var app = this;
    addWaitingClientUrl="/adduser/";
    removeWaitingClientsUrl="";
    waitingClientsUrl="/getWaiting/";



    $http.get(waitingClientsUrl)
      .success(function(data) {
        app.waitingClients = data;
        console.log(data);
      })



    app.addWaitingClient = function(waitingClient) {
        $http.post(addWaitingClientUrl, waitingClient)
          .success(function(data) {
            app.waitingClients = data;
            console.log(data);
          })
        $http.get(waitingClientsUrl)
          .success(function(data) {
            app.waitingClients = data;
            console.log(data);
          })
    }
    app.removeWaitingClient= function(client) {
        console.log(client);
        $http.post(removeWaitingClientUrl, waitingClient)
          .success(function(data) {
            app.waitingClients = data;
          })
    }


    addSeatingClientUrl="data/writedata.json";
    removeSeatingClientsUrl="";
    seatingClientsUrl="data/data2.txt";



    $http.get(seatingClientsUrl)
      .success(function(data) {
        app.seatingClients = data;
      })

    app.addWaitingClient1 = function(client) {
        alert("yo");
        alert(seatingClient.name);
        $http.post(addSeatingClientUrl, SeatingClient)
          .success(function(data) {
            app.seatingClients = data;
            console.log(data);
          })
    }
    app.addSeatingClient = function(client) {
        $http.get(addSeatingClientUrl)
          .success(function(data) {
            app.seatingClients = data;
            console.log(data);
          })
    }
    app.removeSeatingClient= function(client) {
        console.log(client);
        $http.post(removeSeatingClientUrl, seatingClient)
          .success(function(data) {
            app.seatingClients = data;
          })
    }


    addTakeAwayClientUrl="data/writedata.json";
    removeTakeAwayClientsUrl="";
    takeAwayClientsUrl="data/data3.txt";



    $http.get(takeAwayClientsUrl)
      .success(function(data) {
        app.takeAwayClients = data;
      })

    app.addTakeAwayClient1 = function(client) {
        alert("yo");
        alert(TakeAwayClient.name);
        $http.post(addTakeAwayClientUrl, TakeAwayClient)
          .success(function(data) {
            app.takeAwayClients = data;
            console.log(data);
          })
    }
    app.addTakeAwayClient = function(client) {
        $http.get(addTakeAwayClientUrl)
          .success(function(data) {
            app.takeAwayClients = data;
            console.log(data);
          })
    }
    app.removeSeatingClient= function(client) {
        console.log(client);
        $http.post(removeTakeAwayClientUrl, TakeAwayClient)
          .success(function(data) {
            app.takeAwayClients = data;
          })
    }






    addTableUrl="data/addTable.json";
    removeTableUrl="data/removeTable.json";
    tablesUrl="data/tabledata.json";



    $http.get(tablesUrl)
      .success(function(data) {
        app.tables = data;
      })


    app.removeTable = function(table) {
        $http.post(removeTableUrl, table)
          .success(function(data) {
            app.tables = data;
          })
    }

app.ajaxAddTable=function () {
  alert("hi");
    var checkbox_value = "";
    $(":checkbox").each(function () {
        var ischecked = $(this).is(":checked");
        if (ischecked) {
            checkbox_value += $(this).val() + "|";
        }
    });
    alert(checkbox_value);
    $http.post(addTableUrl, checkbox_value)
          .success(function(data) {
            console.log("done");
          })

    $http.get(tablesUrl)
      .success(function(data) {
        app.tables = data;
      })

  }; 


})