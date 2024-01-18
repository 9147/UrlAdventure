function submit(){
    var code = document.getElementById("code").value;
    var question_id = document.getElementById("question_id").innerHTML;
    var data = {
        "code": code,
        "question_id": question_id,
    };
    console.log(data);
    setRequestHeader();
    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "code/",
        data: data,
        success: function (data) {
            console.log("Success:", data);
            alert("Success")
            window.location.href = "../";
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert("Wrong code try again!!!");
        }
    });
}