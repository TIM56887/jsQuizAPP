<template>
    <section> 
        <div class="xl:container min-h-[800px] text-gray-50 mx-auto flex justify-center items-center flex-col relatvie">
            <div class="text-5xl text-center font-semibold p-1  ">
                <h1>Learn JavaScript Fast by Question</h1>
            </div>
            <router-link to="/question">
                <div class="flex items-center font-semibold text-3xl hover:border p-4 shadow-lg shadow-gray-900 mt-20 rounded hover:text-4xl transition-all duration-100 box hover:mt-10">
                    <div class="test">
                        5 random questions
                    </div>
                    <i class="bi bi-play text-5xl ms-4"></i>
                </div>   
            </router-link>
            <!-- <router-link to="/questionlist">
                <div class="flex items-center font-semibold text-3xl hover:border p-4 shadow-lg shadow-gray-900 mt-20 rounded hover:text-4xl transition-all duration-100 box hover:mt-10">
                    <div class="test">
                        Questions List
                    </div>
                    <i class="bi bi-play text-5xl ms-4"></i>
                </div>   
            </router-link> -->
        </div>
          
    </section>
</template>

<script setup>

</script>

<style scoped>

.box {
    --border-size: 1px;
    --border-angle: 0turn;
    padding: 30px;
    background-image: conic-gradient(
      from var(--border-angle),
      #242424 ,
      #2b2a2a,
      #242424 60%
    ),
    conic-gradient(from var(--border-angle), transparent 95%,rgb(243, 236, 238),  rgb(165, 231, 189));

    background-size: calc(100% - (var(--border-size) * 2))
    calc(100% - (var(--border-size) * 2)),
    cover;
    background-position: center center;
    background-repeat: no-repeat;
    animation: bg-spin 3s linear infinite;
}
.box:hover {
        animation-play-state: paused;
        
}
@keyframes bg-spin {
    to {
      --border-angle: 1turn;
    }
  }
@property --border-angle {
  syntax: "<angle>";
  inherits: true;
  initial-value: 0turn;
}


</style>