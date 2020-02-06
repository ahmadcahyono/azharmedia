$(document).ready(function() {
       let mytable1 = $('#tbnonformal').dataTable({
            searching : false,
            ordering:false,
            paging:false,
            pageLength: 5,
            lengthMenu: [1],
            autoWidth: true,
            info:false,
            lengthChange:false,
            responsive: true,
            "scrollY": 200,
            "scrollX": true,
            
        });

         

        // $('#tbnonformal').on('click', 'tbody .edit-row, tbody tr', function (e) {
        //     // e.preventDafault();  
        //      // e.stopPropagation();
        //      // var $row = $(this).closest('tr');
        //      // let data = mytable1.row($row);
        //     // var data = table.row($row).data();
             
        //      //var name = $row[0] ;
        //      var names = $('td', this).eq(0).text();
        //      var name = $('td', this).eq(1).text();
             
        //      var namee = $('td', this).eq(2).text();
             

             
        //     document.getElementById('xid').value = 1
        //     document.getElementById('xstrata').value = names;
        //     document.getElementById('xlembaga').value = name;
        //     $('#xlulus').val(namee);
        //     alert(namee);
        //     //  swal({
        //     //     title: "You data is?",
        //     //     text: names  + " " + " " + name + " " + namee + " " + named,
        //     //      type: "warning",
        //     //     showCancelButton: true,
        //     //     confirmButtonColor: "#DD6B55",
        //     //     closeOnConfirm: false,
        //     //     closeOnCancel: false 
        //     // });
        //     // $('#DescModal').modal("show");
        //     // $('#modalLabel').modal('show');
        // });


        

    // });

        $('#tbnonformal').on('click', 'tbody .remove-row', function (e) {
                e.stopPropagation();
                let t = $('#tbnonformal').DataTable();
                alert('ddd');
                
                t
                .row( $(this).parents('tr') )
                .remove()
                .draw();
            });



        $('#addRow').on( 'click', function () {
            let end = new Date().getFullYear();
            let start = 1990;
            let arr = Array(end-start+1).fill().map(() =>end--);
            let kata = '<select class="form-control input-block" name="xthn[ ]>';
            arr.forEach(function(a){
                kata += '<option>' + a + '</option>';
            });
            kata += '</select>';

            let actions;
            let t = $('#tbnonformal').DataTable();
            actions = [
                '<button type="button" href="#" class="btn-danger  remove-row"><i class="fa fa-trash-o"></i></button>'
            ].join(' ');

            // data = mytable1.row.add([ '', '', '', actions ]);
            // $row = mytable1.row( data[0] ).nodes().to$();
                
            t.row.add( [
            '<select class="form-control input-block" name="xstrata[ ]">' +
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
            '<input class="form-control input-block" name="xlembaga[ ]" />'
            ,
            kata
            ,
            actions] ).draw( false );
 
        
        } );        
      
    new $.fn.dataTable.FixedHeader( mytable1 );

});