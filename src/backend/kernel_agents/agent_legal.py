"""Legal Agent for the Multi-Agent Custom Automation Engine."""

from typing import Optional, List
from semantic_kernel.functions import KernelFunction
from context.cosmos_memory_kernel import CosmosMemoryContext
from kernel_agents.agent_base import BaseAgent


class LegalAgent(BaseAgent):
    """Legal Agent specialized in legal compliance, contracts, and regulatory matters."""

    @staticmethod
    def default_system_message(agent_name=None) -> str:
        """Return the default system message for the Legal Agent."""
        return """You are a Legal AI Agent specialized in legal matters, compliance, and contract management.
        
Your expertise includes:
- Contract review and analysis
- Legal compliance checking
- Regulatory requirements
- Risk assessment
- Legal documentation
- Privacy and data protection laws
        
You provide accurate legal guidance while always recommending consultation with qualified legal professionals for complex matters.
You are thorough, detail-oriented, and always consider legal risks and compliance requirements."""

    @classmethod
    async def create(
        cls,
        agent_name: str = "Legal_Agent",
        session_id: str = "",
        user_id: str = "",
        memory_store: Optional[CosmosMemoryContext] = None,
        tools: Optional[List[KernelFunction]] = None,
        system_message: Optional[str] = None,
        client=None,
        **kwargs
    ) -> "LegalAgent":
        """Create and initialize a Legal Agent instance."""
        
        if system_message is None:
            system_message = cls.default_system_message(agent_name)
            
        # Create the Azure AI agent definition
        definition = await cls._create_azure_ai_agent_definition(
            agent_name=agent_name,
            instructions=system_message,
            tools=tools,
            client=client
        )
        
        # Create the agent instance
        agent = cls(
            agent_name=agent_name,
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            client=client,
            definition=definition
        )
        
        return agent