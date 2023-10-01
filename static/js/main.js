$(document).ready(function () {
    $("#pred-btn").on('click', function () {
        pForm = new FormData(this.form);

            $.ajax({
                url: '/pred',
                type: 'POST',
                data: pForm,
                processData: false,
                contentType: false,
                success: function (res) {
                    res = parseInt(res)
                    if(res == 0){

                        data=`<p class="alert alert-danger fs-4" role="alert">The wine is of <span class="fw-bold"> Bad Quality <span><p>`
                    }
                    else{
                        data=`<p class="alert alert-success fs-4" role="alert">The wine is of <span class="fw-bold"> Good Quality <span><p>`
                    }
                    $('#res').html(data);
                }

            })

    })
})