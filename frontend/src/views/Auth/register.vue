<template>
    <form class="container mt-5 p-5 border rounded shadow">
        <div class="row justify-content-center align-items-center">
            <div class="col-4 justify-content-center align-items-center">

                <div class="form-group">
                    <label for="exampleInputEmail1">Username</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                        placeholder="Enter Username">
                </div>
                <div class="form-group">
                    <label for="exampleInputEmail1">Email address</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                        placeholder="Enter email">
                    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone
                        else.</small>
                </div>
                <div class="form-group mb-3">
                    <label for="exampleInputPassword1">Password1</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                </div>
                <div class="form-group mb-3">
                    <label for="exampleInputPassword2">Password2</label>
                    <input type="password" class="form-control" id="exampleInputPassword2"
                        placeholder="Confirm Password">
                </div>

                <button type="submit" class="btn btn-primary mt-3">Register</button>
            </div>
        </div>
    </form>
</template>
