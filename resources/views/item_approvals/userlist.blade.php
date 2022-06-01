@extends('layouts.normalPage')

@section('content')

    <!-- Datatables libraries -->
    <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.12.1/css/jquery.dataTables.min.css">
    <script src="https://cdn.datatables.net/1.12.1/js/jquery.dataTables.min.js"></script>


    <div class="container p-10">
        <h1 class="text-3xl font-semibold"> Request List </h1>


        <div class="container mx-auto mt-10 w-full">
            <table id="userlist" class="table table-hover">
                <thead>
                <tr>
                    <th></th>
                    <th>REQUEST ID</th>
                    <th>STAFF ID</th>
                    <th>STAFF NAME</th>
                    <th>REQUEST DATE</th>
                    <!-- SEM PLAN 3 - Modify 'View' TO 'Action' -->
                    <th>ACTION</th>
                </tr>
                </thead>
                <tbody>
                @foreach ($staffinfo as $staff)
                    <tr>
                        <td></td>
                            <td>{{ $staff->req_id }}</td>
                            <td>{{ $staff->staff_id }}</td>
                            <td>{{ $staff->name }}</td>
                            <td>{{ $staff->created_at }}</td>
                            <td class="w-1/5">
                                <form action="itemApprove.blade.php" method="POST">

                                    <a href="/item_approvals/request/{{$staff->req_id }}">
                                        <button class="btn btn-outline-primary" type="button">
                                                <i class="far fa-eye"></i>
                                        </button>

                                        @csrf
                                        @method('DELETE')

                                        <!-- SEM PLAN 2 - Adding Delete button -->
                                        <a href="/item_approvals/delete/{{$staff->req_id}}">
                                        <button
                                            type="button" class="btn btn-outline-danger"
                                            onclick="return confirm('Do you really want to delete?');">
                                             Delete
                                        </button>
                                </form>
                            </td>
                    </tr>
                @endforeach
                </tbody>
            </table>
        </div>
    </div>

    <script type="text/javascript" class="init">
        $(document).ready(function () {
            $('#userlist').DataTable();
        });
    </script>



@endsection
