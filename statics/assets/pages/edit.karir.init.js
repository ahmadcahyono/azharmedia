$(document).ready(function() {
       let mytable1 = $('#tbformal').dataTable({
            searching : false,
            ordering:false,
            paging:false,
            autoWidth: true,
            info:false,
            lengthChange:false,
            responsive: true,
            "scrollY": 300,
            "scrollX": true,
  
        });

        $('#tbformal').on('click', 'tbody .remove-row', function (e) {
                e.stopPropagation();
                let t = $('#tbformal').DataTable();
                alert('ddd');
                
                t
                .row( $(this).parents('tr') )
                .remove()
                .draw();
            });



        $('#addFormal').on( 'click', function () {
            let end = new Date().getFullYear();
            let start = 1990;
            let arr = Array(end-start+1).fill().map(() =>end--);
            let kata = '<select class="form-control input-block name="ythn[ ]>';
            arr.forEach(function(a){
                kata += '<option>' + a + '</option>';
            });
            kata += '</select>';

            let actions;
            let t = $('#tbformal').DataTable();
            actions = [
                '<button type="button" href="#" class="btn-danger  remove-row"><i class="fa fa-trash-o"></i></button>'
            ].join(' ');

            t.row.add( [
            '<select class="form-control input-block" name="ystrata[ ]">' +
            // '<select class="form-control input-block" name="xstrata[ ]">' +
            '<option>Sekolah Dasar</option>' +
            '<option>Sekolah Pertama</option>' +
            '<option>SMU/SMK</option>' +
            '<option>Diploma 1</option>' +
            '<option>Diploma 2</option>' +
            '<option>Diploma 3</option>' +
            '<option>Diploma 4</option>' +
            '<option>Akademi</option>' +
            '<option>Strata 1</option>' +
            '<option>Strata 2</option>' +
            '<option>Strata 3</option>' +
            '</select>',
            '<input class="form-control input-block" name="yalmamater[ ]" />'
            ,
            kata
            ,
            actions] ).draw( false );
 
        
        } );        
      
    // new $.fn.dataTable.FixedHeader( mytable1 );

});