from .llm_loader import NODE_CLASS_MAPPINGS as LLM_LOADER_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as LLM_LOADER_DISPLAY_MAPPINGS
from .image_generation import NODE_CLASS_MAPPINGS as IMAGE_GENERATION_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as IMAGE_GENERATION_DISPLAY_MAPPINGS
from .image_understanding import NODE_CLASS_MAPPINGS as IMAGE_UNDERSTANDING_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as IMAGE_UNDERSTANDING_DISPLAY_MAPPINGS
from .model_loader import NODE_CLASS_MAPPINGS as MODEL_LOADER_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as MODEL_LOADER_DISPLAY_MAPPINGS
from .openai_compatible_loader import NODE_CLASS_MAPPINGS as OPENAI_COMPATIBLE_LOADER_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as OPENAI_COMPATIBLE_LOADER_DISPLAY_MAPPINGS

# 合并所有节点映射
NODE_CLASS_MAPPINGS = {
    **LLM_LOADER_MAPPINGS,
    **IMAGE_GENERATION_MAPPINGS,
    **IMAGE_UNDERSTANDING_MAPPINGS,
    **MODEL_LOADER_MAPPINGS,
    **OPENAI_COMPATIBLE_LOADER_MAPPINGS
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **LLM_LOADER_DISPLAY_MAPPINGS,
    **IMAGE_GENERATION_DISPLAY_MAPPINGS,
    **IMAGE_UNDERSTANDING_DISPLAY_MAPPINGS,
    **MODEL_LOADER_DISPLAY_MAPPINGS,
    **OPENAI_COMPATIBLE_LOADER_DISPLAY_MAPPINGS
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]