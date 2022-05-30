@extends('layouts.normalPage')

@section('content')


    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript" src="{{ asset('approve.js') }}"></script>
    <div class="container pt-5">
        <div class="center">
            <h1> Request List </h1>
            <hr>
            <form action="itemApprove.blade.php" method="POST">
                 <!-- SEM PLAN 1 - Adding Searching Bar -->

                 <form action="/search" method="POST" role="search">
                    {{ csrf_field() }}
                    <div class="input-group">
                        <input type="text" class="form-control" name="q"
                            placeholder="Search"> <span class="input-group-btn">
                            <button type="submit" class="btn btn-default">
                                <span class="glyphicon glyphicon-search"></span>
                            </button>
                        </span>
                    </div>
                </form>
                <br>
                @csrf
                <table class="table table-hover">
                    <tr>
                        <th>REQUEST ID</th>
                        <th>STAFF ID</th>
                        <th>STAFF NAME</th>
                        <th>REQUEST DATE</th>
                        <!-- SEM PLAN 3 - Modify 'View' TO 'Action' -->
                        <th>ACTION</th>
                    </tr>
                    @foreach ($staffinfo as $staff)
                        <tr>
                            <td>{{ $staff->req_id }}</td>
                            <td>{{ $staff->staff_id }}</td>
                            <td>{{ $staff->name }}</td>
                            <td>{{ $staff->created_at }}</td>
                            <td><a href="/item_approvals/request/{{ $staff->req_id }}"><button
                                        class="btn btn-outline-primary" type="button">
                                        <i class="far fa-eye"></i>
                                    </button>
                                    &nbsp;
                                <!-- SEM PLAN 2 - Adding Delete button -->
                                <a href="/item_approvals/delete/{{$staff->req_id}}"><button
                                        type="button" class="btn btn-outline-danger"
                                        onclick="return confirm('Do you really want to delete?');">
                                        Delete
                                    </button>
                            </td>
                        </tr>
                    @endforeach
                </table>
            </form>
        </div>
    </div>
@endsection
