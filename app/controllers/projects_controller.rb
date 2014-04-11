class ProjectsController < ApplicationController

  #Basic Search

  has_scope :lead_department
  has_scope :status

  def index
    @projects = apply_scopes(Project).all
  end

  def show
    @project = Project.find params[:id]
  end
end
