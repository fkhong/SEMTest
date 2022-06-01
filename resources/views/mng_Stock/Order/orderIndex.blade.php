@extends('layouts.withDatatable')

@section('content')
    <link rel="stylesheet" type="text/css" href="{{ asset('css/mng_Stock/mng_Stock.css') }}">
    <script type="text/javascript" src="{{ asset('js/mng_Stock/mng_Stock.js') }}"></script>

    <div class="container pt-4">
        <h2>Manage New Stock (Item List)</h2>
        <hr>
    </div>
    <div class="container">
        <div class="row"></div>
    </div>

    <script type="text/javascript" class="init">
        $(document).ready(function() {
            var table = $('#itemList').DataTable({
                initComplete: function() {
                    // Apply the search
                    this.api().columns().every(function() {
                        var that = this;

                        $('input', this.footer()).on('keyup change clear', function() {
                            if (that.search() !== this.value) {
                                that
                                    .search(this.value)
                                    .draw();
                            }
                        });
                    });
                }
            });

        });

    </script>

<div class="container center py-2">
        <a href="/mngNewStck/orderRec"><button class="dt-button" style="float:right;margin-top:20px;margin-left:5px;">Order Record</button></a>
        <a href="/mngNewStck/orderCart"><button class="dt-button" style="float:right;margin-top:20px;margin-left:5px;">Order Cart</button></a>
    </div>

    <form action="/mngNewStck/orderCart" method="POST">
        @csrf
        <div class="container center" style="width:85%; margin-top:10px;border: 1px solid transparent; margin-left:auto;">
            <table style="width:100%; border: 0px solid white;">
                <tr>
                    <td>
                        <table id="itemList" class="display" style="border-collapse:collapse;">
                            <thead>
                                <tr>
                                    <th>No.</th>
                                    <th>Item ID</th>
                                    <th>Item Name</th>
                                    <th>Brand</th>
                                    <th>Inventory Stock</th>
                                    <th>Supplier ID</th>
                                    <th>Supplier Name</th>
                                    <th>Price per Item</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                @foreach ($datas as $data)
                                <?php $itemP = sprintf('%0.2f', $data->item_price);?> <!--For converting the item_price to two decimal places-->
                                    <tr>
                                        <td> {{ $a }} </td>
                                        <td> {{ $data->item_id }} </th>
                                        <td> {{ $data->item_name }} </td>
                                        <td> {{ $data->item_brand }} </td>
                                        <td> {{ $data->item_stock_qty }} </td>
                                        <td> {{ $data->vendor_name }} </td>
                                        <td> {{ $data->vendor_company }} </td>
                                        <td> {{ $itemP }} </td>
                                        <td> <input type="checkbox" name="item_id[]" value="{{ $data->item_id }}"> <input
                                                type="hidden" name="id" value="{{ $a++ }}"></td>
                                    </tr>
                                @endforeach
                            </tbody>
                            <tfoot style="display:none;">
                                <tr>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                </tr>
                            </tfoot>
                        </table>
                    </td>
                </tr>
            </table>
            <input class="right btn btn-primary" style="margin-top:20px;margin-left:5px;" type="submit" value="Add to Cart">
        </div>
    </form>


@endsection
