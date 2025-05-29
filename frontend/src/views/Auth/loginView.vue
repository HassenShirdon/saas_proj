<template>
  <section class="h-100 gradient-form" style="background-color: #eee">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-xl-6">
          <div class="card rounded-3 text-black">
            <div class="card-body p-md-5 mx-md-4 flex-grow-1">
              <form>
                <p>Please login to your account</p>

                <div data-mdb-input-init class="form-outline mb-4">
                  <input type="email" id="form2Example11" class="form-control"
                    placeholder="Phone number or email address" />
                  <label class="form-label" for="form2Example11">Username</label>
                </div>

                <div data-mdb-input-init class="form-outline mb-4">
                  <input type="password" id="form2Example22" class="form-control" />
                  <label class="form-label" for="form2Example22">Password</label>
                </div>

                <div class="text-center pt-1 mb-5 pb-1">
                  <button data-mdb-button-init data-mdb-ripple-init
                    class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="button">
                    Log in
                  </button>
                  <a class="text-muted p-2" href="#!">Forgot password?</a>
                </div>

                <div class="d-flex align-items-center justify-content-center pb-4">
                  <p class="mb-0 me-2">Don't have an account?</p>
                  <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-outline-danger">
                    Create new
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.gradient-custom-2 {
  /* fallback for old browsers */
  background: #fccb90;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
}

@media (min-width: 768px) {
  .gradient-form {
    height: 100vh !important;
  }
}

@media (min-width: 769px) {
  .gradient-custom-2 {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
  }
}

.card-body {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
