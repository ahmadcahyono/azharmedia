$(document).ready(function() {
       let mytable1 = $('#tbkeluarga').dataTable({
            searching : false,
            ordering:false,
            paging:false,
            pageLength: 5,
            lengthMenu: [5],
            autoWidth: true,
            info:false,
            lengthChange:false,
            responsive: true,
            // "scrollY": 200,
            // "scrollX": true,
            
        });


        $('#tbkeluarga').on('click', 'tbody .edit-row, tbody tr', function (e) {
                let t = $('#tbkeluarga').DataTable();
                
                
                
        });
        
        $('#tbkeluarga').on('click', 'tbody .remove-row', function (e) {
                e.stopPropagation();
                let t = $('#tbkeluarga').DataTable();
                alert('ddd');
                
                t
                .row( $(this).parents('tr') )
                .remove()
                .draw();
        });




});