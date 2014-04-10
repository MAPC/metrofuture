class ProjectsController < ApplicationController

  #Basic Search

  has_scope :by_lead_department
  has_scope :by_status

  def index
    @projects = apply_scopes(Project).all
  end

  def show
    @project = Project.find params[:id]
  end
end
