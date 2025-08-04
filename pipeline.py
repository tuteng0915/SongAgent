from acestep.pipeline_ace_step import ACEStepPipeline

pipe = ACEStepPipeline(
    device_id=0,
    dtype="bfloat16",
    torch_compile=True,
)
